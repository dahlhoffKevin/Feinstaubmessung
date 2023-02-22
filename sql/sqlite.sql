CREATE TABLE "wetter" (
	"id" INTEGER NOT NULL UNIQUE,
	"sensor_id" INTEGER NOT NULL UNIQUE,
	"sensor_type" TEXT,
	"location" TEXT,
	"latitude" REAL,
	"longitude" REAL,
	"timestemp" TEXT
	"temperatur" REAL,
	"humidity" REAL,
	PRIMARY KEY ("id")
);

CREATE TABLE "feinstaub" (
	"id" INTEGER NOT NULL UNIQUE,
	"sensor_id" INTEGER NOT NULL UNIQUE,
	"sensor_type" TEXT,
	"location" TEXT,
	"latitude" REAL,
	"longitude" REAL,
	"timestemp" TEXT,
	"P1" REAL,
	"durP1" REAL,
	"ratioP1" REAL,
	"P2" REAL,
	"durP2" REAL,
	"ratioP2" REAL,
	PRIMARY KEY ("id")
);