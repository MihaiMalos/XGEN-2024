import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CsvHandlerComponent } from './uploader.component';

describe('UploaderComponent', () => {
  let component: CsvHandlerComponent;
  let fixture: ComponentFixture<CsvHandlerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CsvHandlerComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CsvHandlerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
