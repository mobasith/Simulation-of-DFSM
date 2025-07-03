import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DfsmInputComponent } from './dfsm-input.component';

describe('DfsmInputComponent', () => {
  let component: DfsmInputComponent;
  let fixture: ComponentFixture<DfsmInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DfsmInputComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DfsmInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
