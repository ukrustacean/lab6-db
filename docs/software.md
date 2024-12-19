# Реалізація інформаційного та програмного забезпечення

## Короткий зміст

- [Реалізація інформаційного та програмного забезпечення](#реалізація-інформаційного-та-програмного-забезпечення)
  - [SQL-скрипт для створення та початкового наповнення бази даних](#sql-скрипт-для-створення-та-початкового-наповнення-бази-даних)
  - [RESTful сервіс для управління даними](#restful-сервіс-для-управління-даними)


 
## SQL-скрипт для створення на початкового наповнення бази даних

```mysql

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Role` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`User` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `account_creation_date` DATETIME NOT NULL,
  `last_login_date` DATETIME NULL,
  `Role_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `Role_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `fk_User_Role_idx` (`Role_id` ASC) VISIBLE,
  CONSTRAINT `fk_User_Role`
    FOREIGN KEY (`Role_id`)
    REFERENCES `mydb`.`Role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Category` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Data` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `content` VARCHAR(255) NOT NULL,
  `upload_date` DATETIME NOT NULL,
  `last_edit_date` DATETIME NULL,
  `Category_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `Category_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  INDEX `fk_Data_Category1_idx` (`Category_id` ASC) VISIBLE,
  CONSTRAINT `fk_Data_Category1`
    FOREIGN KEY (`Category_id`)
    REFERENCES `mydb`.`Category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Comment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Comment` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NOT NULL,
  `creation_date` DATETIME NOT NULL,
  `User_id` INT UNSIGNED NOT NULL,
  `Data_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Comment_User1_idx` (`User_id` ASC) VISIBLE,
  INDEX `fk_Comment_Data1_idx` (`Data_id` ASC) VISIBLE,
  CONSTRAINT `fk_Comment_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Comment_Data1`
    FOREIGN KEY (`Data_id`)
    REFERENCES `mydb`.`Data` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NULL,
  `Role_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `Role_id`),
  INDEX `fk_Permission_Role1_idx` (`Role_id` ASC) VISIBLE,
  CONSTRAINT `fk_Permission_Role1`
    FOREIGN KEY (`Role_id`)
    REFERENCES `mydb`.`Role` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Session` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `login_time` DATETIME NOT NULL,
  `logout_time` DATETIME NOT NULL,
  `User_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `User_id`),
  INDEX `fk_Session_User1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Session_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Log` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `action_type` VARCHAR(45) NOT NULL,
  `action_date` DATETIME NOT NULL,
  `User_id` INT UNSIGNED NOT NULL,
  `Data_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Log_User1_idx` (`User_id` ASC) VISIBLE,
  INDEX `fk_Log_Data1_idx` (`Data_id` ASC) VISIBLE,
  CONSTRAINT `fk_Log_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Log_Data1`
    FOREIGN KEY (`Data_id`)
    REFERENCES `mydb`.`Data` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Access`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Access` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `access_type` VARCHAR(45) NOT NULL,
  `User_id` INT UNSIGNED NOT NULL,
  `Data_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Access_User1_idx` (`User_id` ASC) VISIBLE,
  INDEX `fk_Access_Data1_idx` (`Data_id` ASC) VISIBLE,
  CONSTRAINT `fk_Access_User1`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Access_Data1`
    FOREIGN KEY (`Data_id`)
    REFERENCES `mydb`.`Data` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `mydb`.`Role`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`Role` (`id`, `name`, `description`) VALUES (1, 'admin', 'responsible for managing and publishing data, can import new data, organize it into sets, add metadata, and publish it for other users to access');
INSERT INTO `mydb`.`Role` (`id`, `name`, `description`) VALUES (2, 'user', 'creates tools and APIs to integrate data with the system, develops and tests modules for working with data and ensure compatibility with other services');

COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`User`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`User` (`id`, `name`, `password`, `email`, `account_creation_date`, `last_login_date`, `Role_id`) VALUES (1, 'Shcherbakov_Illia', 'Wandestes', 'gilua5568@gmail.com', '2024-11-20 15:13:59', '2024-11-27 08:13:57', 1);
INSERT INTO `mydb`.`User` (`id`, `name`, `password`, `email`, `account_creation_date`, `last_login_date`, `Role_id`) VALUES (2, 'Dereviankin_Ivan', 'Vanya', 'ukrustacean@gmail.com', '2024-11-20 10:26:43', '2024-11-27 15:26:38', 1);
INSERT INTO `mydb`.`User` (`id`, `name`, `password`, `email`, `account_creation_date`, `last_login_date`, `Role_id`) VALUES (3, 'Chernyshova_Maria', 'Maria', 'marija.tchernishowa@gmail.com', '2024-11-20 15:11:28', '2024-12-20 19:45:17', 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`Category`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`Category` (`id`, `name`, `description`) VALUES (1, 'Gamecon', 'Information related to Gamecon from all time');
INSERT INTO `mydb`.`Category` (`id`, `name`, `description`) VALUES (2, 'Movies', 'Movies and cartoons');
INSERT INTO `mydb`.`Category` (`id`, `name`, `description`) VALUES (3, 'Education for kids', 'Puzzles for kids');

COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`Data`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`Data` (`id`, `name`, `content`, `upload_date`, `last_edit_date`, `Category_id`) VALUES (1, 'Puzzles', 'Puzzles types', '2023-06-18 17:42:21', '2023-08-14 09:42:36', 3);
INSERT INTO `mydb`.`Data` (`id`, `name`, `content`, `upload_date`, `last_edit_date`, `Category_id`) VALUES (2, 'Movies', 'Shrek', '2023-02-10 20:17:22', NULL, 1);
INSERT INTO `mydb`.`Data` (`id`, `name`, `content`, `upload_date`, `last_edit_date`, `Category_id`) VALUES (3, 'Cartoons', 'Ben-10', '2023-09-26 19:11:19', '2019-16-13 09:30:01', 3);
INSERT INTO `mydb`.`Data` (`id`, `name`, `content`, `upload_date`, `last_edit_date`, `Category_id`) VALUES (4, 'Game of the year 2024', 'Stalker 2', '2024-12-20 19:30:00', NULL, 3);
INSERT INTO `mydb`.`Data` (`id`, `name`, `content`, `upload_date`, `last_edit_date`, `Category_id`) VALUES (5, 'Games', 'Games list', '2016-06-14 11:59:54', NULL, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`Comment`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`Comment` (`id`, `content`, `creation_date`, `User_id`, `Data_id`) VALUES (1, 'Shrek is sus', '2024-09-05 08:33:19', 2, 2);
INSERT INTO `mydb`.`Comment` (`id`, `content`, `creation_date`, `User_id`, `Data_id`) VALUES (2, 'Thank you for adding my favorite childhood movie', '2024-10-06 12:13:42', 1, 3);
INSERT INTO `mydb`.`Comment` (`id`, `content`, `creation_date`, `User_id`, `Data_id`) VALUES (3, 'Im really surprised', '2024-12-20 21:13:19, 3, 4);

COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`Permission`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (1, 'read', 'for admin', 1);
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (2, 'edit', 'for admin', 1);
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (3, 'upload', 'for admin', 1);
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (4, 'download', 'for admin', 1);
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (5, 'delete', 'for admin', 1);
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (6, 'read', 'for user', 2);
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (7, 'edit', 'for user', 2);
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (8, 'upload', 'for uses', 2);
INSERT INTO `mydb`.`Permission` (`id`, `name`, `description`, `Role_id`) VALUES (9, 'download', 'for user', 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`Session`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`Session` (`id`, `login_time`, `logout_time`, `User_id`) VALUES (1, '2024-11-27 08:13:57', '2024-11-27 11:16:42', 1);
INSERT INTO `mydb`.`Session` (`id`, `login_time`, `logout_time`, `User_id`) VALUES (2, '2024-11-27 05:26:38', '2024-11-27 11:01:41', 2);
INSERT INTO `mydb`.`Session` (`id`, `login_time`, `logout_time`, `User_id`) VALUES (3, '2024-12-20 15:45:17', '2024-12-20 19:45:17', 3);


COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`Log`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`Log` (`id`, `action_type`, `action_date`, `User_id`, `Data_id`) VALUES (1, 'upload', '2023-02-26 10:26:54', 1, 1);
INSERT INTO `mydb`.`Log` (`id`, `action_type`, `action_date`, `User_id`, `Data_id`) VALUES (2, 'edit', '2023-03-12 12:24:28', 2, 1);
INSERT INTO `mydb`.`Log` (`id`, `action_type`, `action_date`, `User_id`, `Data_id`) VALUES (3, 'upload', '2023-05-12 19:15:12', 3, 2);
INSERT INTO `mydb`.`Log` (`id`, `action_type`, `action_date`, `User_id`, `Data_id`) VALUES (4, 'upload', '2023-11-30 16:17:29', 2, 3);
INSERT INTO `mydb`.`Log` (`id`, `action_type`, `action_date`, `User_id`, `Data_id`) VALUES (5, 'edit', '2024-10-16 17:30:56', 3, 3);
INSERT INTO `mydb`.`Log` (`id`, `action_type`, `action_date`, `User_id`, `Data_id`) VALUES (6, 'upload', '2023-01-12 17:26:17', 1, 2);


COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`Access`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`Access` (`id`, `access_type`, `User_id`, `Data_id`) VALUES (1, 'read', 1, 3);
INSERT INTO `mydb`.`Access` (`id`, `access_type`, `User_id`, `Data_id`) VALUES (2, 'edit', 1, 3);
INSERT INTO `mydb`.`Access` (`id`, `access_type`, `User_id`, `Data_id`) VALUES (3, 'delete', 1, 3);
INSERT INTO `mydb`.`Access` (`id`, `access_type`, `User_id`, `Data_id`) VALUES (4, 'read', 3, 2);
INSERT INTO `mydb`.`Access` (`id`, `access_type`, `User_id`, `Data_id`) VALUES (5, 'edit', 2, 1);
INSERT INTO `mydb`.`Access` (`id`, `access_type`, `User_id`, `Data_id`) VALUES (6, 'read', 2, 1);
INSERT INTO `mydb`.`Access` (`id`, `access_type`, `User_id`, `Data_id`) VALUES (7, 'edit', 3, 2);

COMMIT;

```

## RESTfull сервіс для управління даними

main.py 

```mysql

from fastapi import FastAPI
from database import engine, Base
from routes import router
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)

```

database.py 

```mysql

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_PASSWORD

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:12345678@127.0.0.1:3306/mydb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

```

models.py

```mysql

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime, timezone, timedelta


class Data(Base):
    __tablename__ = 'Data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, unique=True)
    content = Column(String)
    upload_date = Column(DateTime, default=lambda: datetime.now(timezone.utc) + timedelta(hours=2))
    last_edit_date = Column(DateTime, nullable=True)
    category_id = Column(Integer, ForeignKey('Category.id'))

    category = relationship("Category", back_populates="data_items")


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)

    data_items = relationship("Data", back_populates="category")


```

schemas.py

```mysql

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DataCreate(BaseModel):
    id: Optional[int] = None
    name: str
    content: str
    upload_date: Optional[datetime] = None
    last_edit_date: Optional[datetime] = None
    category_id: int


class CategoryCreate(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None


class DataResponse(DataCreate):
    class Config:
        orm_mode = True


class CategoryResponse(CategoryCreate):
    class Config:
        orm_mode = True


class CategoryPatch(BaseModel):
    id: int = None
    name: str = None
    description: Optional[str] = None


class DataPatch(BaseModel):
    id: int = None
    name: str = None
    content: str = None
    upload_date: datetime = None
    last_edit_date: Optional[datetime] = None
    category_id: int = None


```

routes.py

```mysql

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Data, Category
from schemas import DataCreate, CategoryCreate, DataResponse, CategoryResponse, CategoryPatch, DataPatch
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/data/", response_model=List[DataResponse])
async def read_data(db: Session = Depends(get_db)):
    return db.query(Data).all()


@router.get("/data/{data_id}", response_model=DataResponse)
async def read_data_by_id(data_id: int, db: Session = Depends(get_db)):
    db_data = db.query(Data).filter(data_id == Data.id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="The data with the specified ID was not found")
    return db_data


@router.post("/data/", response_model=DataResponse)
async def create_data(data: DataCreate, db: Session = Depends(get_db)):
    id_data = db.query(Data).filter(data.id == Data.id).first()
    if id_data:
        raise HTTPException(status_code=400, detail="The data with this ID already exists")

    name_data = db.query(Data).filter(data.name == Data.name).first()
    if name_data:
        raise HTTPException(status_code=400, detail="The data with this name already exists")

    id_category = db.query(Category).filter(data.category_id == Category.id).first()
    if not id_category:
        raise HTTPException(status_code=400, detail="The category with the specified ID was not found")

    db_data = Data(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    return db_data


@router.put("/data/{data_id}", response_model=DataResponse)
async def update_data(data_id: int, data: DataCreate, db: Session = Depends(get_db)):
    db_data = db.query(Data).filter(data_id == Data.id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="The data with the specified ID was not found")

    id_data = db.query(Data).filter(data.id == Data.id, data_id != Data.id).first()
    if id_data:
        raise HTTPException(status_code=400, detail="The data with this ID already exists")

    name_data = db.query(Data).filter(data.name == Data.name, data_id != Data.id).first()
    if name_data:
        raise HTTPException(status_code=400, detail="The data with this name already exists")

    if data.category_id:
        id_category = db.query(Category).filter(data.category_id == Category.id).first()
        if not id_category:
            raise HTTPException(status_code=400, detail="The category with the specified ID was not found")

    for key, value in data.dict().items():
        setattr(db_data, key, value)

    db.commit()
    db.refresh(db_data)
    return db_data


@router.delete("/data/{data_id}", response_model=DataResponse)
async def delete_data(data_id: int, db: Session = Depends(get_db)):
    db_data = db.query(Data).filter(data_id == Data.id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="The data with the specified ID was not found")

    db.delete(db_data)
    db.commit()
    return db_data


@router.patch("/data/{data_id}", response_model=DataResponse)
async def patch_data(data_id: int, data: DataPatch, db: Session = Depends(get_db)):
    db_data = db.query(Data).filter(data_id == Data.id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="The data with the specified ID was not found")

    updated_fields = data.dict(exclude_unset=True)

    if 'id' in updated_fields and updated_fields['id'] != data_id:
        id_data = db.query(Data).filter(Data.id == updated_fields['id']).first()
        if id_data:
            raise HTTPException(status_code=400, detail="The data with this ID already exists")

    if 'name' in updated_fields:
        name_data = db.query(Data).filter(Data.name == updated_fields['name'], data_id != Data.id).first()
        if name_data:
            raise HTTPException(status_code=400, detail="The data with this name already exists")

    if 'category_id' in updated_fields:
        category = db.query(Category).filter(Category.id == updated_fields['category_id']).first()
        if not category:
            raise HTTPException(status_code=400, detail="The category with the specified ID was not found")

    for key, value in updated_fields.items():
        setattr(db_data, key, value)

    db.commit()
    db.refresh(db_data)
    return db_data


@router.get("/category/", response_model=List[CategoryResponse])
async def read_category(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Category).offset(skip).limit(limit).all()


@router.get("/category/{category_id}", response_model=CategoryResponse)
async def read_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(category_id == Category.id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="The category with the specified ID was not found")
    return db_category


@router.post("/category/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    existing_category = db.query(Category).filter(category.id == Category.id).first()
    if existing_category:
        raise HTTPException(status_code=400, detail="The category with this ID already exists")

    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


@router.put("/category/{category_id}", response_model=CategoryResponse)
async def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(category_id == Category.id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="The category with the specified ID was not found")

    id_data = db.query(Data).filter(category.id == Category.id, category_id != Category.id).first()
    if id_data:
        raise HTTPException(status_code=400, detail="The category with this ID already exists")

    for key, value in category.dict().items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)
    return db_category


@router.delete("/category/{category_id}", response_model=CategoryResponse)
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(category_id == Category.id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="The category with the specified ID was not found")

    related_data = db.query(Data).filter(category_id == Data.category_id).first()
    if related_data:
        raise HTTPException(status_code=403, detail="Cannot delete category with associated data")

    db.delete(db_category)
    db.commit()
    return db_category


@router.patch("/category/{category_id}", response_model=CategoryResponse)
async def patch_category(category_id: int, category: CategoryPatch, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(category_id == Category.id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="The category with the specified ID was not found")

    updated_data = category.dict(exclude_unset=True)

    if 'id' in updated_data and updated_data['id'] != category_id:
        id_category = db.query(Category).filter(Category.id == updated_data['id']).first()
        if id_category:
            raise HTTPException(status_code=400, detail="The category with this ID already exists")

    for key, value in updated_data.items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)
    return db_category


```

