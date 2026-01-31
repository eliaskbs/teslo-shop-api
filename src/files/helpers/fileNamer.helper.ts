import { v4 as uuid } from 'uuid';

type FileFilterCallback = (error: Error | null, acceptFile: string) => void;

export const fileNamer = (
  req: Express.Request,
  file: Express.Multer.File,
  callback: FileFilterCallback,
) => {
  const fileExtension = file.mimetype.split('/')[1];

  const fileName = `${uuid()}.${fileExtension}`;

  return callback(null, fileName);
};
