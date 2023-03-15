CREATE TABLE "wetter" (
	"id" TEXT NOT NULL,
	"sensor_id" INTEGER,
	"sensor_type" TEXT,
	"location" TEXT,
	"latitude" REAL,
	"longitude" REAL,
	"timestemp" TEXT,
	"temperatur" REAL,
	"humidity" REAL,
	PRIMARY KEY ("id")
);

CREATE TABLE "feinstaub" (
	"id" TEXT NOT NULL,
	"sensor_id" INTEGER,
	"sensor_type" TEXT,
	"location" TEXT,
	"latitude" REAL,
	"longitude" REAL,
	"timestemp" TEXT,
	"P1" REAL,
	"durP1" TEXT,
	"ratioP1" TEXT,
	"P2" REAL,
	"durP2" TEXT,
	"ratioP2" TEXT,
	PRIMARY KEY ("id")
);