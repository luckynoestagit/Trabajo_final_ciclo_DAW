import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewnewsletterSection } from './newnewsletter-section';

describe('NewnewsletterSection', () => {
  let component: NewnewsletterSection;
  let fixture: ComponentFixture<NewnewsletterSection>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NewnewsletterSection]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewnewsletterSection);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
