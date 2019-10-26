import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampesinoDetailComponent } from './campesino-detail.component';

describe('CampesinoDetailComponent', () => {
  let component: CampesinoDetailComponent;
  let fixture: ComponentFixture<CampesinoDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampesinoDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampesinoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
