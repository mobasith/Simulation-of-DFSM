import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { inject } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DfaApiService {
  private apiUrl = 'https://simulation-of-dfsm-production.up.railway.app/';

  constructor(public http: HttpClient = inject(HttpClient)) {}

  simulateDfa(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/simulate`, data);
  }
}
