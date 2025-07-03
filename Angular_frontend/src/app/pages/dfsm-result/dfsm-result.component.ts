import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dfsm-result',
  standalone: true,
  imports: [],
  templateUrl: './dfsm-result.component.html',
  styleUrl: './dfsm-result.component.css'
})
export class DfsmResultComponent implements OnInit{
  result:any;
  pdfUrl: string = '';

  constructor(public router: Router) {}

  ngOnInit(): void {
    const stored = localStorage.getItem('dfa-result');
    if (!stored) {
      this.router.navigate(['/']);
      return;
    }
  this.result = JSON.parse(stored);
  this.pdfUrl = `http://localhost:8000${this.result.pdf_path}`; // Adjust if you host backend elsewhere
  }
  

}
