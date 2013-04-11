# Generated automatically from Makefile.in by configure.
#-----------------------------------------------------------------------------
#
# NcFTP vis makefile for the platform macosx10.8.3, on the host joaos-macbook-pro.local.
#
#-----------------------------------------------------------------------------

CC=gcc
CFLAGS=-D_REENTRANT -O2 -W -Wall -Wno-format-y2k -static-libgcc
#CC=gcc
#CFLAGS=-O2 -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wmissing-declarations -Wshadow -Wbad-function-cast -Wwrite-strings -Wconversion
CPPFLAGS=-I/Users/joaovasques/Duplicity/ncftp-3.2.5 -I../libncftp -I../Strn -I../sio -I/Users/joaovasques/Duplicity/ncftp-3.2.5 -I/Users/joaovasques/Duplicity/ncftp-3.2.5/libncftp -I/Users/joaovasques/Duplicity/ncftp-3.2.5/sio -I/Users/joaovasques/Duplicity/ncftp-3.2.5/Strn
prefix=/usr/local
exec_prefix=${prefix}
BINDIR=${exec_prefix}/bin
SYSCONFDIR=${prefix}/etc
SOCKS_LIBS=
CURSESLIBS=-lncurses
LIBS=$(CURSESLIBS)  $(SOCKS_LIBS)
STRIP=strip
LDFLAGS=-L../libncftp -L../Strn -L../sio -L/Users/joaovasques/Duplicity/ncftp-3.2.5/libncftp -L/Users/joaovasques/Duplicity/ncftp-3.2.5/sio -L/Users/joaovasques/Duplicity/ncftp-3.2.5/Strn

# Any -D definitions:
DEFS=-Dvis -DO_S=\"macosx10.8.3\" -DNCFTPPATH=\"$(BINDIR)/ncftp\" -DSYSCONFDIR=\"$(SYSCONFDIR)\" -DHAVE_CONFIG_H -DMACOSX=10803

DPROGS=../bin/ncftpbookmarks

all: $(DPROGS)
	-@echo 'Done making NcFTP full-screen utilities.'

../bin/ncftpbookmarks: bmed.c wgets.o wutil.o pref.o preffw.o trace.o util.o bookmark.o version.o bmed.h wgets.h syshdrs.h ../libncftp/libncftp.a
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) bmed.c wgets.o wutil.o pref.o preffw.o trace.o util.o bookmark.o version.o -o ../bin/ncftpbookmarks $(LDFLAGS) -lncftp -lStrn -lsio $(LIBS)
	-@$(STRIP) ../bin/ncftpbookmarks
	-@/bin/rm -rf ../bin/ncftpbookmarks.dSYM

bookmark.o: ../ncftp/bookmark.c ../ncftp/bookmark.h syshdrs.h
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) ../ncftp/bookmark.c -c

pref.o: ../ncftp/pref.c ../ncftp/pref.h syshdrs.h
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) ../ncftp/pref.c -c

preffw.o: ../ncftp/preffw.c ../ncftp/pref.h syshdrs.h
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) ../ncftp/preffw.c -c

trace.o: ../ncftp/trace.c ../ncftp/trace.h syshdrs.h
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) ../ncftp/trace.c -c

util.o: ../ncftp/util.c ../ncftp/util.h syshdrs.h
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) ../ncftp/util.c -c

version.o: ../ncftp/version.c
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) ../ncftp/version.c -c

wutil.o: wutil.c wutil.h syshdrs.h
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) wutil.c -c

wgets.o: wgets.c wgets.h syshdrs.h
	@/Users/joaovasques/Duplicity/ncftp-3.2.5/ccdv $(CC) $(CFLAGS) $(DEFS) $(CPPFLAGS) wgets.c -c

clean:
	/bin/rm -rf $(DPROGS) *.o core *.pch SunWS_cache

PACKAGE=Makefile.in bmed.c bmed.h syshdrs.h wgets.c wgets.h wutil.c wutil.h

TMPDIR=/tmp
TARDIR=vis

tarcp:
	-@mkdir -p $(TMPDIR)/TAR/$(TARDIR)
	-@chmod ga+r $(PACKAGE)
	-@chmod 755 $(TMPDIR)/TAR/$(TARDIR)
	cp -pr $(PACKAGE) $(TMPDIR)/TAR/$(TARDIR)
