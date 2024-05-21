import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CsvHandlerComponent } from './uploader/uploader.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,CsvHandlerComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'csv-uploader';
}
