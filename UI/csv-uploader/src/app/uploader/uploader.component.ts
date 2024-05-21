
import { Component, OnInit } from '@angular/core';
import *  as Papa from 'papaparse';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import {MatSelectModule} from '@angular/material/select';
import { MatFormField } from '@angular/material/select';
import { MatOption } from '@angular/material/select';
import { table } from 'console';
import { Observable } from 'rxjs';
@Component({
  selector: 'app-uploader',
  standalone: true,
  imports: [FormsModule,CommonModule,MatSelectModule,MatFormField,MatOption],
  templateUrl: './uploader.component.html',
  styleUrl: './uploader.component.scss'
})
export class CsvHandlerComponent implements OnInit{
  csvData: string[][] = [];
  labelIndex: number | null = null;
  tableName: string = '';
  dataSets: string[] = [];
  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.fetchDataSets();
  }
  getDataSets(): Observable<any> {
    return this.http.get<string[]>('http://127.0.0.1:5000/get_datasets');
  }
  fetchDataSets(): void {
    this.getDataSets().subscribe(
      data => {
        this.dataSets = data;
      },
      error => {
        console.error('Error fetching datasets:', error);
      }
    );
  }
  fetchTable() {
    this.http.post('http://127.0.0.1:5000//get_table', { table_name: this.tableName }, { responseType: 'text' }).subscribe(
      data => {
        Papa.parse(data, {
          complete: (result: Papa.ParseResult<string[]>) => {
            this.csvData = result.data;
            this.identifyLabelIndex();
          },
          header: false
        });
      },
      error => {
        console.error('Error fetching table:', error);
      }
    );
  }
  identifyLabelIndex() {
    if (this.csvData.length > 0) {
      this.labelIndex = this.csvData[0].indexOf('label');
    }
  }
  compareFn(optionValue: number, cellValue: string): boolean {
    return optionValue === parseInt(cellValue, 10);
  }
  onCellEdit(event: any, rowIndex: number, cellIndex: number) {
    if (this.labelIndex !== null && cellIndex === this.labelIndex) {
      this.csvData[rowIndex][cellIndex] = event.value;
    }
  }  
  saveCSV() {
    const csv = Papa.unparse(this.csvData);
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const formData = new FormData();
    formData.append('csvFile', blob, 'modified.csv');
    formData.append('table_name', this.tableName);

    fetch('http://127.0.0.1:5000/save-csv', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to save CSV file on server');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Handle success response from server
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
}