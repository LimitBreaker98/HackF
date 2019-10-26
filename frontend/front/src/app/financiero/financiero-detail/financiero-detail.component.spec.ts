import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FinancieroDetailComponent } from './financiero-detail.component';

describe('FinancieroDetailComponent', () => {
  let component: FinancieroDetailComponent;
  let fixture: ComponentFixture<FinancieroDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FinancieroDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FinancieroDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
