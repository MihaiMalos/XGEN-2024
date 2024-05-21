
import { Component } from '@angular/core';
import *  as Papa from 'papaparse';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import {MatSelectModule} from '@angular/material/select';
import { MatFormField } from '@angular/material/select';
import { MatOption } from '@angular/material/select';
@Component({
  selector: 'app-uploader',
  standalone: true,
  imports: [CommonModule,MatSelectModule,MatFormField,MatOption],
  templateUrl: './uploader.component.html',
  styleUrl: './uploader.component.scss'
})
export class CsvHandlerComponent {
  csvData: string[][] = [];
  labelIndex: number | null = null;

  onFileChange(event: any) {
    const file = event.target.files[0];
    if (file) {
      Papa.parse(file, {
        complete: (result: Papa.ParseResult<string[]>) => {
          this.csvData = result.data;
          this.identifyLabelIndex();
        },
        header: false
      });
    }
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
  }  saveCSV() {
    const csv = Papa.unparse(this.csvData);
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', 'modified.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
}