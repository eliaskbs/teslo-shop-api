import {
  BadRequestException,
  Controller,
  Get,
  Param,
  Post,
  Res,
  UploadedFile,
  UploadedFiles,
  UseInterceptors,
} from '@nestjs/common';
import { FilesService } from './files.service';
import { FileInterceptor, FilesInterceptor } from '@nestjs/platform-express';
import { diskStorage } from 'multer';
import { fileNamer, fileFilter } from './helpers';
import express from 'express';
import { ConfigService } from '@nestjs/config';

@Controller('files')
export class FilesController {
  constructor(
    private readonly filesService: FilesService,
    private readonly configService: ConfigService,
  ) {}

  @Get('product/:imageName')
  findProdcutImage(
    @Res() res: express.Response,
    @Param('imageName') imageName: string,
  ) {
    const path = this.filesService.getStaticProductImage(imageName);
    res.sendFile(path);
  }

  @Post('product')
  @UseInterceptors(
    FileInterceptor('file', {
      fileFilter: fileFilter,
      // limits: { fieldNameSize: 100 },
      storage: diskStorage({
        destination: './static/products',
        filename: fileNamer,
      }),
    }),
  )
  uploadFileImage(@UploadedFile() file: Express.Multer.File) {
    if (!file) {
      throw new BadRequestException('Make sure the file is valid image');
    }

    const secureUrl = `${this.configService.get('HOST_API')}/api/files/product/${file.filename}`;

    return {
      fileName: secureUrl,
    };
  }

  @Post('uploadProducts')
  @UseInterceptors(FilesInterceptor('files'))
  uploadProductsFile(@UploadedFiles() files: Array<Express.Multer.File>) {
    if (!files) {
      throw new BadRequestException('');
    }

    files.forEach((file) => {
      console.log(file.destination);
    });
  }
}
