#!/usr/bin/perl

use DBI;
use strict;
use CGI qw(:standard);
use JSON;

my $driver = "SQLite";
my $database = "test.db";

# DBI:$driver:dbname:$database" should be "DBI:$driver:dbname=$database"


my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 })
   or die $DBI::errstr;


print header('application/json');

my $stmt;

my $search = "". $parameters->param('search');

if ( $search eq "" )
{
    $stmt = qq(SELECT id, date, time, desc FROM APPOINTMENT;);
}
else
{
    $stmt = qq(SELECT id, date, time, desc FROM APPOINTMENT WHERE desc LIKE ? ;);
}

my $sth = $dbh->prepare( $stmt );

my $preparedStatements = $dbh->prepare($statements);

if ( $isEmpty eq "no" ) {
    $preparedStatements->bind_param( 1, "%" . $search . "%" );
}


my $rv = $sth->execute() or die $DBI::errstr;

if($rv < 0) {
   print $DBI::errstr;
}

my @datas;

while ( my @row = $preparedStatements->fetchrow_array() ) {
    my %item = (
        "id" => $row[0],
        "date"        => $row[1],
        "time"        => $row[2],
        "description"        => $row[3]
    );

    push(@datas, \%item);
}

print $json->encode( \@datas ) . "\n";


print "Operation done successfully\n";
$dbh->disconnect();
