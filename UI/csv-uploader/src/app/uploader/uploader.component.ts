
import { Component } from '@angular/core';
import *  as Papa from 'papaparse';
import { NgIf } from '@angular/common';
import { NgFor } from '@angular/common';
@Component({
  selector: 'app-uploader',
  standalone: true,
  imports: [NgIf,NgFor],
  templateUrl: './uploader.component.html',
  styleUrl: './uploader.component.scss'
})
export class CsvHandlerComponent {
  csvData: string[][] = [];

  onFileChange(event: any) {
    const file = event.target.files[0];
    if (file) {
      Papa.parse(file, {
        complete: (result: Papa.ParseResult<string[]>) => {
          this.csvData = result.data;
        },
        header: false
      });
    }
  }
  onCellEdit(event: any, rowIndex: number, cellIndex: number) {
    this.csvData[rowIndex][cellIndex] = event.target.value;
  }
  saveCSV() {
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