import { Component } from '@angular/core';


@Component({
  selector: 'app-pagina-principal',
  imports: [],
  templateUrl: './pagina-principal.html',
  styleUrl: './pagina-principal.css',
})
export class PaginaPrincipal {
  scrollLeft() {
    const container = document.querySelector('.product-container') as HTMLElement;
    container.scrollBy({ left: -320, behavior: 'smooth' });
  }

  scrollRight() {
    const container = document.querySelector('.product-container') as HTMLElement;
    container.scrollBy({ left: 320, behavior: 'smooth' });
  }
}
