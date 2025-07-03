import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DfsmResultComponent } from './dfsm-result.component';

describe('DfsmResultComponent', () => {
  let component: DfsmResultComponent;
  let fixture: ComponentFixture<DfsmResultComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DfsmResultComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DfsmResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
