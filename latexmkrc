#!/usr/bin/env perl

$ENV{'TEXINPUTS'} = ":$project//";

uplatex('misc/references.tex');
