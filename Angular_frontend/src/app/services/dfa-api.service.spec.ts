import { TestBed } from '@angular/core/testing';

import { DfaApiService } from './dfa-api.service';

describe('DfaApiService', () => {
  let service: DfaApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DfaApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
