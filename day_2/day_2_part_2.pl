#!/usr/bin/perl
use strict;
use warnings;

my $validPasswords = 0;
my $regex = qr/(\d+)-(\d+)\s([a-zA-Z]):\s([a-zA-Z]+)/mp;
my $filename = 'input.txt';
open(my $fh, '<:encoding(UTF-8)', $filename)
    or die "Could not open file '$filename' $!";

while (my $row = <$fh>){
    chomp $row;
    if ( $row =~ /$regex/g ) {
        my $charPos1 = $1;
        my $charPos2 = $2;
        my $charToCheck = $3;
        my $charString = $4;

        my $offset = 0;
        my $result = index($charString, $charToCheck, $offset);

        my @charIndexes = [];

        while ($result != -1) {
            push(@charIndexes, $result);
            $offset = $result + 1;
            $result = index($charString, $charToCheck, $offset);
        }
        
        if ( $charPos1-1 ~~ @charIndexes xor $charPos2-1 ~~ @charIndexes){
            $validPasswords += 1;
        }
    }  
}

print ("Valid Passwords: $validPasswords\n");
