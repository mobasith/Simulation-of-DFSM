import { Routes } from '@angular/router';
import { DfsmInputComponent } from './pages/dfsm-input/dfsm-input.component';
import { DfsmResultComponent } from './pages/dfsm-result/dfsm-result.component';

export const routes: Routes = [
    {path:'',component:DfsmInputComponent},
    {path:'result',component:DfsmResultComponent}
];
