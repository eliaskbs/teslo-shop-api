import { Injectable } from '@nestjs/common';
import { ProductsService } from '../products/products.service';
import { initialData } from './data/seed.data';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from '../auth/entities/user.entity';
import * as bcrypt from 'bcrypt';

@Injectable()
class SeedService {
  constructor(
    private readonly productService: ProductsService,
    @InjectRepository(User) private readonly userRepository: Repository<User>,
  ) {}

  async runSeed() {
    await this.deleteAllTables();
    const userAdmin = await this.insertUsers();
    await this.inserNewProducts(userAdmin);
    return 'SEED EXECUTE';
  }

  private async insertUsers() {
    const users = initialData.users;
    const arrayUsers: User[] = [];

    users.forEach((user) => {
      const { password, ...userData } = user;
      arrayUsers.push(
        this.userRepository.create({
          ...userData,
          password: bcrypt.hashSync(password, 10),
        }),
      );
    });
    const dbUsers = await this.userRepository.save(arrayUsers);

    return dbUsers[0];
  }

  private async deleteAllTables() {
    await this.productService.removeAllProduct();

    const queryBuilder = this.userRepository.createQueryBuilder();
    await queryBuilder.delete().where({}).execute();
  }

  private async inserNewProducts(user: User) {
    await this.productService.removeAllProduct();

    const products = initialData.products;

    const insertPromises: any[] = [];

    products.forEach((product) =>
      insertPromises.push(this.productService.create(product, user)),
    );
    await Promise.all(insertPromises);

    return true;
  }
}

export default SeedService;
