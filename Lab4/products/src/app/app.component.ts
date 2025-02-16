import { Component } from '@angular/core';
import { ProductsComponent } from './components/products/products.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [ProductsComponent], 
})
export class AppComponent {
  title = 'kaspi-products';
}
