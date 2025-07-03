import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DfaApiService } from '../../services/dfa-api.service';

@Component({
  selector: 'app-dfsm-input',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './dfsm-input.component.html',
  styleUrl: './dfsm-input.component.css'
})
export class DfsmInputComponent {

  dfaForm = this.fb.group({
    states: ['', Validators.required],
    alphabet: ['', Validators.required],
    start: ['', Validators.required],
    accept: ['', Validators.required],
    inputString: ['', Validators.required],
    transitions: ['', Validators.required],
  });

  constructor(
    private fb: FormBuilder,
    private api: DfaApiService,
    private router: Router
  ) {}

  onSubmit() {
    if (this.dfaForm.invalid) return;

    const form = this.dfaForm.value;

    const payload = {
      states: form.states?.split(',').map(s => s.trim()),
      alphabet: form.alphabet?.split(',').map(s => s.trim()),
      start: form.start?.trim(),
      accept: form.accept?.split(',').map(s => s.trim()),
      input_string: form.inputString?.trim(),
      transitions: this.parseTransitions(form.transitions || '')
    };

    this.api.simulateDfa(payload).subscribe((response: any) => {
      localStorage.setItem('dfa-result', JSON.stringify(response));
      this.router.navigate(['/result']);
    });
  }

  parseTransitions(input: string): any {
    const lines = input.split('\n');
    const transitions: Record<string, Record<string, string>> = {};
    lines.forEach(line => {
      if (!line.trim()) return; // ✅ Ignore empty lines
      const [from, symbol, to] = line.split(',').map(s => s.trim());
      if (!transitions[from]) transitions[from] = {};
      transitions[from][symbol] = to;
    });
    return transitions;
  }
  
  }


