#!/usr/bin/perl
use strict;
use warnings;

my $filename = 'input.txt';
open(my $fh, '<:encoding(UTF-8)', $filename)
    or die "Could not open file '$filename' $!";

my $validPasswords = 0;

while (my $row = <$fh>){
    chomp $row;

    my $regex = qr/(\d+)-(\d+)\s([a-zA-Z]):\s([a-zA-Z]+)/mp;

    if ( $row =~ /$regex/g ) {
        my $minChars = $1;
        my $maxChars = $2;
        my $charToCheck = $3;
        my $charString = $4;
        my @c = $charString =~ /$charToCheck/g;
        my $charCount = @c;

        if ($charCount >= $minChars && $charCount <= $maxChars) {
            $validPasswords += 1;
        }
    }  
}

print ("Valid Passwords: $validPasswords\n");
