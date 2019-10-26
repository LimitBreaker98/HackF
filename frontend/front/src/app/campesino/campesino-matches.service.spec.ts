import { TestBed } from '@angular/core/testing';

import { CampesinoMatchesService } from './campesino-matches.service';

describe('CampesinoMatchesService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CampesinoMatchesService = TestBed.get(CampesinoMatchesService);
    expect(service).toBeTruthy();
  });
});
