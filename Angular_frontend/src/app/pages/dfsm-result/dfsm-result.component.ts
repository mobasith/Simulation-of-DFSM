import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dfsm-result',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dfsm-result.component.html',
  styleUrl: './dfsm-result.component.css'
})
export class DfsmResultComponent implements OnInit{
  getPdfFileName(): string {
    if (!this.pdfUrl) return 'dfa_output.pdf';
    return this.pdfUrl.split('/').pop() || 'dfa_output.pdf';
  }
  result:any;
  pdfUrl: string = '';

  constructor(public router: Router) {}

  ngOnInit(): void {
    if (typeof window !== 'undefined' && localStorage) {
      const stored = localStorage.getItem('dfa-result');
      if (!stored) {
        this.router.navigate(['/']);
        return;
      }
  
      this.result = JSON.parse(stored);
      this.pdfUrl = `https://simulation-of-dfsm-production.up.railway.app${this.result.pdf_path}`;

    } else {
      console.error('localStorage is not available.');
      this.router.navigate(['/']);
    }
  }
  
  

}
