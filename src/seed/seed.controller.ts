import { Controller, Get } from '@nestjs/common';
import SeedService from './seed.service';
import { Auth } from '../auth/decorators/auth.decorator';

@Controller('seed')
export class SeedController {
  constructor(private seedService: SeedService) {}

  @Get()
  // @Auth(ValidRolesInterface.admin)
  execute() {
    return this.seedService.runSeed();
  }
}
