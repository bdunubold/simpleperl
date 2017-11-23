#!/usr/bin/perl

use DBI;
use strict;

my $driver   = "SQLite";
my $database = "test.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 })
   or die $DBI::errstr;
print "Opened database successfully\n";


my $stmt = qq(
CREATE TABLE APPOINTMENT (
    ID INT PRIMARY KEY     NOT NULL,
    DESC           TEXT    NOT NULL,
    DATE           CHAR(50)     NOT NULL,
    TIME           CHAR(50)     NOT NULL
););

my $rv = $dbh->do($stmt);
if($rv < 0) {
   print $DBI::errstr;
} else {
   print "Table created successfully\n";
}
$dbh->disconnect();
