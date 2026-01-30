import { Injectable } from '@nestjs/common';
import { ProductsService } from '../products/products.service';
import { initialData } from './data/seed.data';

@Injectable()
export class SeedService {
  constructor(private readonly productService: ProductsService) {}

  async runSeed() {
    await this.inserNewProducts();
    return 'SEED EXECUTE';
  }

  private async inserNewProducts() {
    await this.productService.removeAllProduct();

    const products = initialData.products;

    const insertPromises: any[] = [];

    products.forEach((product) =>
      insertPromises.push(this.productService.create(product)),
    );
    await Promise.all(insertPromises);

    return true;
  }
}
