#!/usr/bin/perl

use CGI;
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


my $cgi = CGI->new();

my $id = $cgi->param('id');
my $date = $cgi->param('date');
my $time = $cgi->param('time');
my $description = $cgi->param('description');

my $stmt = qq(INSERT INTO APPOINTMENT(id, date, time, desc)
           VALUES ('" . $id . "','" . $date . "','" . $time . "' ,'" . $description . "'););
my $rv = $dbh->do($stmt) or die $DBI::errstr;

$dbh->disconnect();
