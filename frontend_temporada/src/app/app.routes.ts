import { Routes } from '@angular/router';
import {PaginaPrincipal} from './features/pagina-principal/pagina-principal';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./layouts/main-layout/main-layout').then(c => c.MainLayout),
    children: [
      {path: "",loadComponent: () => import('./features/pagina-principal/pagina-principal').then(c => c.PaginaPrincipal),
      }
    ]
  },
];
