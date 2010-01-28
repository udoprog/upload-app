
import os;

base_lookups = {
  '.3dmf': 'x-world/x-3dmf',
  '.3dm': 'x-world/x-3dmf',
  '.aab': 'application/x-authorware-bin',
  '.aam': 'application/x-authorware-map',
  '.a': 'application/octet-stream',
  '.aas': 'application/x-authorware-seg',
  '.abc': 'text/vnd.abc',
  '.acgi': 'text/html',
  '.afl': 'video/animaflex',
  '.ai': 'application/postscript',
  '.ai': 'application/postscript',
  '.aif': 'audio/aiff',
  '.aif': 'audio/x-aiff',
  '.aifc': 'audio/aiff',
  '.aifc': 'audio/x-aiff',
  '.aiff': 'audio/aiff',
  '.aiff': 'audio/x-aiff',
  '.aim': 'application/x-aim',
  '.aip': 'text/x-audiosoft-intra',
  '.ani': 'application/x-navi-animation',
  '.aos': 'application/x-nokia-9000-communicator-add-on-software',
  '.aps': 'application/mime',
  '.arc': 'application/octet-stream',
  '.arj': 'application/arj',
  '.arj': 'application/octet-stream',
  '.art': 'image/x-jg',
  '.asf': 'video/x-ms-asf',
  '.asm': 'text/x-asm',
  '.asp': 'text/asp',
  '.asx': 'application/x-mplayer2',
  '.asx': 'video/x-ms-asf',
  '.asx': 'video/x-ms-asf-plugin',
  '.au': 'audio/basic',
  '.au': 'audio/x-au',
  '.avi': 'application/x-troff-msvideo',
  '.avi': 'video/avi',
  '.avi': 'video/msvideo',
  '.avi': 'video/x-msvideo',
  '.avs': 'video/avs-video',
  '.bat': 'text/plain',
  '.bcpio': 'application/x-bcpio',
  '.bin': 'application/mac-binary',
  '.bin': 'application/macbinary',
  '.bin': 'application/octet-stream',
  '.bin': 'application/x-binary',
  '.bin': 'application/x-macbinary',
  '.bm': 'image/bmp',
  '.bmp': 'image/bmp',
  '.bmp': 'image/x-ms-bmp',
  '.bmp': 'image/x-windows-bmp',
  '.boo': 'application/book',
  '.book': 'application/book',
  '.boz': 'application/x-bzip2',
  '.bsh': 'application/x-bsh',
  '.bz2': 'application/x-bzip2',
  '.bz': 'application/x-bzip',
  '.cat': 'application/vnd.ms-pki.seccat',
  '.ccad': 'application/clariscad',
  '.cco': 'application/x-cocoa',
  '.cc': 'text/plain',
  '.cc': 'text/x-c',
  '.cdf': 'application/cdf',
  '.cdf': 'application/x-cdf',
  '.cdf': 'application/x-netcdf',
  '.cer': 'application/pkix-cert',
  '.cer': 'application/x-x509-ca-cert',
  '.cha': 'application/x-chat',
  '.chat': 'application/x-chat',
  '.class': 'application/java',
  '.class': 'application/java-byte-code',
  '.class': 'application/x-java-class',
  '.com': 'application/octet-stream',
  '.com': 'text/plain',
  '.conf': 'text/plain',
  '.cpio': 'application/x-cpio',
  '.cpio': 'application/x-cpio',
  '.cpp': 'text/x-c',
  '.cpt': 'application/mac-compactpro',
  '.cpt': 'application/x-compactpro',
  '.cpt': 'application/x-cpt',
  '.crl': 'application/pkcs-crl',
  '.crl': 'application/pkix-crl',
  '.crt': 'application/pkix-cert',
  '.crt': 'application/x-x509-ca-cert',
  '.crt': 'application/x-x509-user-cert',
  '.csh': 'application/x-csh',
  '.csh': 'text/x-script.csh',
  '.css': 'application/x-pointplus',
  '.css': 'text/css',
  '.c': 'text/plain',
  '.c++': 'text/plain',
  '.c': 'text/x-c',
  '.cxx': 'text/plain',
  '.dcr': 'application/x-director',
  '.deepv': 'application/x-deepv',
  '.def': 'text/plain',
  '.der': 'application/x-x509-ca-cert',
  '.dif': 'video/x-dv',
  '.dir': 'application/x-director',
  '.dll': 'application/octet-stream',
  '.dl': 'video/dl',
  '.dl': 'video/x-dl',
  '.doc': 'application/msword',
  '.dot': 'application/msword',
  '.dp': 'application/commonground',
  '.drw': 'application/drafting',
  '.dump': 'application/octet-stream',
  '.dvi': 'application/x-dvi',
  '.dv': 'video/x-dv',
  '.dwf': 'drawing/x-dwf (old)',
  '.dwf': 'model/vnd.dwf',
  '.dwg': 'application/acad',
  '.dwg': 'image/vnd.dwg',
  '.dwg': 'image/x-dwg',
  '.dxf': 'application/dxf',
  '.dxf': 'image/vnd.dwg',
  '.dxf': 'image/x-dwg',
  '.dxr': 'application/x-director',
  '.elc': 'application/x-bytecode.elisp (compiled elisp)',
  '.elc': 'application/x-elc',
  '.el': 'text/x-script.elisp',
  '.eml': 'message/rfc822',
  '.env': 'application/x-envoy',
  '.eps': 'application/postscript',
  '.es': 'application/x-esrehber',
  '.etx': 'text/x-setext',
  '.evy': 'application/envoy',
  '.evy': 'application/x-envoy',
  '.exe': 'application/octet-stream',
  '.f77': 'text/x-fortran',
  '.f90': 'text/plain',
  '.f90': 'text/x-fortran',
  '.fdf': 'application/vnd.fdf',
  '.fif': 'application/fractals',
  '.fif': 'image/fif',
  '.fli': 'video/fli',
  '.fli': 'video/x-fli',
  '.flo': 'image/florian',
  '.flx': 'text/vnd.fmi.flexstor',
  '.fmf': 'video/x-atomic3d-feature',
  '.for': 'text/plain',
  '.for': 'text/x-fortran',
  '.fpx': 'image/vnd.fpx',
  '.fpx': 'image/vnd.net-fpx',
  '.frl': 'application/freeloader',
  '.f': 'text/plain',
  '.f': 'text/x-fortran',
  '.funk': 'audio/make',
  '.g3': 'image/g3fax',
  '.gif': 'image/gif',
  '.gl': 'video/gl',
  '.gl': 'video/x-gl',
  '.gsd': 'audio/x-gsm',
  '.gsm': 'audio/x-gsm',
  '.gsp': 'application/x-gsp',
  '.gss': 'application/x-gss',
  '.gtar': 'application/x-gtar',
  '.gtar': 'application/x-gtar',
  '.g': 'text/plain',
  '.gz': 'application/x-compressed',
  '.gz': 'application/x-gzip',
  '.gzip': 'application/x-gzip',
  '.gzip': 'multipart/x-gzip',
  '.hdf': 'application/x-hdf',
  '.help': 'application/x-helpfile',
  '.hgl': 'application/vnd.hp-hpgl',
  '.hh': 'text/plain',
  '.hh': 'text/x-h',
  '.hlb': 'text/x-script',
  '.hlp': 'application/hlp',
  '.hlp': 'application/x-helpfile',
  '.hlp': 'application/x-winhelp',
  '.hpg': 'application/vnd.hp-hpgl',
  '.hpgl': 'application/vnd.hp-hpgl',
  '.hqx': 'application/binhex',
  '.hqx': 'application/binhex4',
  '.hqx': 'application/mac-binhex',
  '.hqx': 'application/mac-binhex40',
  '.hqx': 'application/x-binhex40',
  '.hqx': 'application/x-mac-binhex40',
  '.hta': 'application/hta',
  '.htc': 'text/x-component',
  '.h': 'text/plain',
  '.h': 'text/x-h',
  '.htmls': 'text/html',
  '.html': 'text/html',
  '.html': 'text/html',
  '.htm': 'text/html',
  '.htt': 'text/webviewhtml',
  '.htx': 'text/html',
  '.ice': 'x-conference/x-cooltalk',
  '.ico': 'image/x-icon',
  '.idc': 'text/plain',
  '.ief': 'image/ief',
  '.iefs': 'image/ief',
  '.iges': 'application/iges',
  '.iges': 'model/iges',
  '.igs': 'application/iges',
  '.igs': 'model/iges',
  '.ima': 'application/x-ima',
  '.imap': 'application/x-httpd-imap',
  '.inf': 'application/inf',
  '.ins': 'application/x-internett-signup',
  '.ip': 'application/x-ip2',
  '.isu': 'video/x-isvideo',
  '.it': 'audio/it',
  '.iv': 'application/x-inventor',
  '.ivr': 'i-world/i-vrml',
  '.ivy': 'application/x-livescreen',
  '.jam': 'audio/x-jam',
  '.java': 'text/plain',
  '.java': 'text/x-java-source',
  '.jav': 'text/plain',
  '.jav': 'text/x-java-source',
  '.jcm': 'application/x-java-commerce',
  '.jfif': 'image/jpeg',
  '.jfif': 'image/pjpeg',
  '.jfif-tbnl': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.jpeg': 'image/pjpeg',
  '.jpe': 'image/jpeg',
  '.jpe': 'image/pjpeg',
  '.jpg': 'image/jpeg',
  '.jpg': 'image/jpg',
  '.jpg': 'image/pjpeg',
  '.jps': 'image/x-jps',
  '.js': 'application/x-javascript',
  '.js': 'application/x-javascript',
  '.jut': 'image/jutvision',
  '.kar': 'audio/midi',
  '.kar': 'music/x-karaoke',
  '.ksh': 'application/x-ksh',
  '.ksh': 'text/plain',
  '.ksh': 'text/x-script.ksh',
  '.la': 'audio/nspaudio',
  '.la': 'audio/x-nspaudio',
  '.lam': 'audio/x-liveaudio',
  '.latex': 'application/x-latex',
  '.lha': 'application/lha',
  '.lha': 'application/octet-stream',
  '.lha': 'application/x-lha',
  '.lhx': 'application/octet-stream',
  '.list': 'text/plain',
  '.lma': 'audio/nspaudio',
  '.lma': 'audio/x-nspaudio',
  '.log': 'text/plain',
  '.lsp': 'application/x-lisp',
  '.lsp': 'text/x-script.lisp',
  '.lst': 'text/plain',
  '.lsx': 'text/x-la-asf',
  '.ltx': 'application/x-latex',
  '.lzh': 'application/octet-stream',
  '.lzh': 'application/x-lzh',
  '.lzx': 'application/lzx',
  '.lzx': 'application/octet-stream',
  '.lzx': 'application/x-lzx',
  '.m1v': 'video/mpeg',
  '.m2a': 'audio/mpeg',
  '.m2v': 'video/mpeg',
  '.m3u': 'audio/x-mpequrl',
  '.man': 'application/x-troff-man',
  '.map': 'application/x-navimap',
  '.mar': 'text/plain',
  '.mbd': 'application/mbedlet',
  '.mc$': 'application/x-magic-cap-package-1.0',
  '.mcd': 'application/mcad',
  '.mcd': 'application/x-mathcad',
  '.mcf': 'image/vasa',
  '.mcf': 'text/mcf',
  '.mcp': 'application/netmc',
  '.me': 'application/x-troff-me',
  '.me': 'application/x-troff-me',
  '.mht': 'message/rfc822',
  '.mhtml': 'message/rfc822',
  '.mid': 'application/x-midi',
  '.mid': 'audio/midi',
  '.mid': 'audio/x-mid',
  '.mid': 'audio/x-midi',
  '.midi': 'application/x-midi',
  '.midi': 'audio/midi',
  '.midi': 'audio/midi',
  '.midi': 'audio/x-mid',
  '.midi': 'audio/x-midi',
  '.midi': 'music/crescendo',
  '.midi': 'x-music/x-midi',
  '.mid': 'music/crescendo',
  '.mid': 'x-music/x-midi',
  '.mif': 'application/x-frame',
  '.mif': 'application/x-mif',
  '.mime': 'message/rfc822',
  '.mime': 'www/mime',
  '.mjf': 'audio/x-vnd.audioexplosion.mjuicemediafile',
  '.mjpg': 'video/x-motion-jpeg',
  '.mm': 'application/base64',
  '.mm': 'application/x-meme',
  '.mme': 'application/base64',
  '.mod': 'audio/mod',
  '.mod': 'audio/x-mod',
  '.moov': 'video/quicktime',
  '.movie': 'video/x-sgi-movie',
  '.mov': 'video/quicktime',
  '.mp2': 'audio/mpeg',
  '.mp2': 'audio/x-mpeg',
  '.mp2': 'video/mpeg',
  '.mp2': 'video/x-mpeg',
  '.mp2': 'video/x-mpeq2a',
  '.mp3': 'audio/mpeg3',
  #'.mp3': 'audio/x-mpeg-3',
  '.mpa': 'audio/mpeg',
  '.mpa': 'video/mpeg',
  '.mpc': 'application/x-project',
  '.mpeg': 'video/mpeg',
  '.mpeg': 'video/mpeg',
  '.mpe': 'video/mpeg',
  '.mpga': 'audio/mpeg',
  '.mpg': 'audio/mpeg',
  '.mpg': 'video/mpeg',
  '.mpp': 'application/vnd.ms-project',
  '.mpt': 'application/x-project',
  '.mpv': 'application/x-project',
  '.mpx': 'application/x-project',
  '.mrc': 'application/marc',
  '.ms': 'application/x-troff-ms',
  '.ms': 'application/x-troff-ms',
  '.m': 'text/plain',
  '.m': 'text/x-m',
  '.mv': 'video/x-sgi-movie',
  '.my': 'audio/make',
  '.mzz': 'application/x-vnd.audioexplosion.mzz',
  '.nap': 'image/naplps',
  '.naplps': 'image/naplps',
  '.nc': 'application/x-netcdf',
  '.nc': 'application/x-netcdf',
  '.ncm': 'application/vnd.nokia.configuration-message',
  '.niff': 'image/x-niff',
  '.nif': 'image/x-niff',
  '.nix': 'application/x-mix-transfer',
  '.nsc': 'application/x-conference',
  '.nvd': 'application/x-navidoc',
  '.nws': 'message/rfc822',
  '.o': 'application/octet-stream',
  '.obj': 'application/octet-stream',
  '.oda': 'application/oda',
  '.omc': 'application/x-omc',
  '.omcd': 'application/x-omcdatamaker',
  '.omcr': 'application/x-omcregerator',
  '.p10': 'application/pkcs10',
  '.p10': 'application/x-pkcs10',
  '.p12': 'application/pkcs-12',
  '.p12': 'application/x-pkcs12',
  '.p7a': 'application/x-pkcs7-signature',
  '.p7c': 'application/pkcs7-mime',
  '.p7c': 'application/x-pkcs7-mime',
  '.p7m': 'application/pkcs7-mime',
  '.p7m': 'application/x-pkcs7-mime',
  '.p7r': 'application/x-pkcs7-certreqresp',
  '.p7s': 'application/pkcs7-signature',
  '.part': 'application/pro_eng',
  '.pas': 'text/pascal',
  '.pbm': 'image/x-portable-bitmap',
  '.pcl': 'application/vnd.hp-pcl',
  '.pcl': 'application/x-pcl',
  '.pct': 'image/pict',
  '.pct': 'image/x-pict',
  '.pcx': 'image/x-pcx',
  '.pdb': 'chemical/x-pdb',
  '.pdf': 'application/pdf',
  '.pfunk': 'audio/make',
  '.pfunk': 'audio/make.my.funk',
  '.pfx': 'application/x-pkcs12',
  '.pgm': 'image/x-portable-graymap',
  '.pgm': 'image/x-portable-greymap',
  '.pic': 'image/pict',
  '.pict': 'image/pict',
  '.pict': 'image/pict',
  '.pkg': 'application/x-newton-compatible-pkg',
  '.pko': 'application/vnd.ms-pki.pko',
  '.pl': 'text/plain',
  '.pl': 'text/plain',
  '.pl': 'text/x-script.perl',
  '.plx': 'application/x-pixclscript',
  '.pm4': 'application/x-pagemaker',
  '.pm5': 'application/x-pagemaker',
  '.pm': 'image/x-xpixmap',
  '.pm': 'text/x-script.perl-module',
  '.png': 'image/png',
  '.pnm': 'application/x-portable-anymap',
  '.pnm': 'image/x-portable-anymap',
  '.pot': 'application/mspowerpoint',
  '.pot': 'application/vnd.ms-powerpoint',
  '.pov': 'model/x-pov',
  '.ppa': 'application/vnd.ms-powerpoint',
  '.ppm': 'image/x-portable-pixmap',
  '.pps': 'application/mspowerpoint',
  '.pps': 'application/vnd.ms-powerpoint',
  '.ppt': 'application/mspowerpoint',
  '.ppt': 'application/powerpoint',
  '.ppt': 'application/vnd.ms-powerpoint',
  '.ppt': 'application/x-mspowerpoint',
  '.ppz': 'application/mspowerpoint',
  '.pre': 'application/x-freelance',
  '.prt': 'application/pro_eng',
  '.ps': 'application/postscript',
  '.ps': 'application/postscript',
  '.psd': 'application/octet-stream',
  '.p': 'text/x-pascal',
  '.pvu': 'paleovu/x-pv',
  '.pwz': 'application/vnd.ms-powerpoint',
  '.pyc': 'applicaiton/x-bytecode.python',
  '.pyc': 'application/x-python-code',
  '.pyo': 'application/x-python-code',
  '.py': 'text/x-python',
  '.py': 'text/x-script.phyton',
  '.qcp': 'audio/vnd.qcelp',
  '.qd3d': 'x-world/x-3dmf',
  '.qd3': 'x-world/x-3dmf',
  '.qif': 'image/x-quicktime',
  '.qtc': 'video/x-qtc',
  '.qtif': 'image/x-quicktime',
  '.qti': 'image/x-quicktime',
  '.qt': 'video/quicktime',
  '.qt': 'video/quicktime',
  '.ra': 'audio/x-pn-realaudio',
  '.ra': 'audio/x-pn-realaudio',
  '.ra': 'audio/x-pn-realaudio-plugin',
  '.ra': 'audio/x-realaudio',
  '.rar': 'application/x-rar-compressed',
  '.ram': 'application/x-pn-realaudio',
  '.ram': 'audio/x-pn-realaudio',
  '.ras': 'application/x-cmu-raster',
  '.ras': 'image/cmu-raster',
  '.ras': 'image/x-cmu-raster',
  '.rast': 'image/cmu-raster',
  '.rdf': 'application/xml',
  '.rexx': 'text/x-script.rexx',
  '.rf': 'image/vnd.rn-realflash',
  '.rgb': 'image/x-rgb',
  '.rm': 'application/vnd.rn-realmedia',
  '.rm': 'audio/x-pn-realaudio',
  '.rmi': 'audio/mid',
  '.rmm': 'audio/x-pn-realaudio',
  '.rmp': 'audio/x-pn-realaudio',
  '.rmp': 'audio/x-pn-realaudio-plugin',
  '.rng': 'application/ringing-tones',
  '.rng': 'application/vnd.nokia.ringing-tone',
  '.rnx': 'application/vnd.rn-realplayer',
  '.roff': 'application/x-troff',
  '.roff': 'application/x-troff',
  '.rp': 'image/vnd.rn-realpix',
  '.rpm': 'audio/x-pn-realaudio-plugin',
  '.rtf': 'application/rtf',
  '.rtf': 'application/x-rtf',
  '.rtf': 'text/richtext',
  '.rt': 'text/richtext',
  '.rt': 'text/vnd.rn-realtext',
  '.rtx': 'application/rtf',
  '.rtx': 'text/richtext',
  '.rv': 'video/vnd.rn-realvideo',
  '.s3m': 'audio/s3m',
  '.saveme': 'application/octet-stream',
  '.sbk': 'application/x-tbook',
  '.scm': 'application/x-lotusscreencam',
  '.scm': 'text/x-script.guiserver-parsed-html',
  '.sgml': 'text/x-sgml',
  '.sgm': 'text/x-sgml',
  '.sh': 'application/x-sh',
  '.shar': 'application/x-shar',
  '.sid': 'audio/x-psid',
  '.sit': 'application/x-sit',
  '.sit': 'application/x-stuffit',
  '.skd': 'application/x-koan',
  '.skm': 'application/x-koan',
  '.skp': 'application/x-koan',
  '.skt': 'application/x-koan',
  '.sl': 'application/x-seelogo',
  '.smi': 'application/smil',
  '.smil': 'application/smil',
  '.snd': 'audio/basic',
  '.snd': 'audio/x-adpcm',
  '.so': 'application/octet-stream',
  '.sol': 'application/solids',
  '.spc': 'application/x-pkcs7-certificates',
  '.spc': 'text/x-speech',
  '.spl': 'application/futuresplash',
  '.spr': 'application/x-sprite',
  '.sprite': 'application/x-sprite',
  '.src': 'application/x-wais-source',
  '.ssi': 'text/x-server-parsed-html',
  '.ssm': 'application/streamingmedia',
  '.sst': 'application/vnd.ms-pki.certstore',
  '.step': 'application/step',
  '.s': 'text/x-asm',
  '.stl': 'application/sla',
  '.stl': 'application/vnd.ms-pki.stl',
  '.stl': 'application/x-navistyle',
  '.stp': 'application/step',
  '.sv4cpio': 'application/x-sv4cpio',
  '.sv4cpio': '/x-sv4cpio',
  '.sv4crc': 'application/x-sv4crc',
  '.sv4crc': 'application/x-sv4crc',
  '.svf': 'image/vnd.dwg',
  '.svf': 'image/x-dwg',
  '.svr': 'application/x-world',
  '.svr': 'x-world/x-svr',
  '.swf': 'application/x-shockwave-flash',
  '.talk': 'text/x-speech',
  '.t': 'application/x-troff',
  '.tar': 'application/x-tar',
  '.tbk': 'application/toolbook',
  '.tbk': 'application/x-tbook',
  '.tcl': 'application/x-tcl',
  '.tcl': 'text/x-script.tcl',
  '.tcsh': 'text/x-script.tcsh',
  '.tex': 'application/x-tex',
  '.texi': 'application/x-texinfo',
  '.texi': 'application/x-texinfo',
  '.texinfo': 'application/x-texinfo',
  '.texinfo':'application/x-texinfo',
  '.text': 'application/plain',
  '.text': 'text/plain',
  '.nfo': 'text/plain',
  '.tgz': 'application/gnutar',
  '.tgz': 'application/x-compressed',
  '.tiff': 'image/tiff',
  '.tiff': 'image/tiff',
  '.tiff': 'image/x-tiff',
  '.tif': 'image/tiff',
  '.tif': 'image/x-tiff',
  '.tr': 'application/x-troff',
  '.tr': 'application/x-troff',
  '.tsi': 'audio/tsp-audio',
  '.tsp': 'application/dsptype',
  '.tsp': 'audio/tsplayer',
  '.tsv': 'text/tab-separated-values',
  '.turbot': 'image/florian',
  '.txt': 'text/plain',
  '.uil': 'text/x-uil',
  '.unis': 'text/uri-list',
  '.uni': 'text/uri-list',
  '.unv': 'application/i-deas',
  '.uris': 'text/uri-list',
  '.uri': 'text/uri-list',
  '.ustar': 'application/x-ustar',
  '.ustar': 'multipart/x-ustar',
  '.uu': 'application/octet-stream',
  '.uue': 'text/x-uuencode',
  '.uu': 'text/x-uuencode',
  '.vcd': 'application/x-cdlink',
  '.vcf': 'application/x-vcard',
  '.vcs': 'text/x-vcalendar',
  '.vda': 'application/vda',
  '.vdo': 'video/vdo',
  '.vew': 'application/groupwise',
  '.vivo': 'video/vivo',
  '.vivo': 'video/vnd.vivo',
  '.viv': 'video/vivo',
  '.viv': 'video/vnd.vivo',
  '.vmd': 'application/vocaltec-media-desc',
  '.vmf': 'application/vocaltec-media-file',
  '.voc': 'audio/voc',
  '.voc': 'audio/x-voc',
  '.vos': 'video/vosaic',
  '.vox': 'audio/voxware',
  '.vqe': 'audio/x-twinvq-plugin',
  '.vqf': 'audio/x-twinvq',
  '.vql': 'audio/x-twinvq-plugin',
  '.vrml': 'application/x-vrml',
  '.vrml': 'model/vrml',
  '.vrml': 'x-world/x-vrml',
  '.vrt': 'x-world/x-vrt',
  '.vsd': 'application/x-visio',
  '.vst': 'application/x-visio',
  '.vsw': 'application/x-visio',
  '.w60': 'application/wordperfect6.0',
  '.w61': 'application/wordperfect6.1',
  '.w6w': 'application/msword',
  '.wav': 'audio/wav',
  '.wav': 'audio/x-wav',
  '.wb1': 'application/x-qpro',
  '.wbmp': 'image/vnd.wap.wbmp',
  '.web': 'application/vnd.xara',
  '.wiz': 'application/msword',
  '.wk1': 'application/x-123',
  '.wmf': 'windows/metafile',
  '.wmlc': 'application/vnd.wap.wmlc',
  '.wmlsc': 'application/vnd.wap.wmlscriptc',
  '.wmls': 'text/vnd.wap.wmlscript',
  '.wml': 'text/vnd.wap.wml',
  '.word': 'application/msword',
  '.wp5': 'application/wordperfect',
  '.wp5': 'application/wordperfect6.0',
  '.wp6': 'application/wordperfect',
  '.wp': 'application/wordperfect',
  '.wpd': 'application/wordperfect',
  '.wpd': 'application/x-wpwin',
  '.wq1': 'application/x-lotus',
  '.wri': 'application/mswrite',
  '.wri': 'application/x-wri',
  '.wrl': 'application/x-world',
  '.wrl': 'model/vrml',
  '.wrl': 'x-world/x-vrml',
  '.wrz': 'model/vrml',
  '.wrz': 'x-world/x-vrml',
  '.wsc': 'text/scriplet',
  '.wsdl': 'text/xml',
  '.wsrc': 'application/x-wais-source',
  '.wtk': 'application/x-wintalk',
  '.xbm': 'image/xbm',
  '.xbm': 'image/x-xbitmap',
  '.xbm': 'image/x-xbm',
  '.xdr': 'video/x-amt-demorun',
  '.xgz': 'xgl/drawing',
  '.xif': 'image/vnd.xiff',
  '.xla': 'application/excel',
  '.xla': 'application/x-excel',
  '.xla': 'application/x-msexcel',
  '.xl': 'application/excel',
  '.xlb': 'application/excel',
  '.xlb': 'application/vnd.ms-excel',
  '.xlb': 'application/x-excel',
  '.xlc': 'application/excel',
  '.xlc': 'application/vnd.ms-excel',
  '.xlc': 'application/x-excel',
  '.xld': 'application/excel',
  '.xld': 'application/x-excel',
  '.xlk': 'application/excel',
  '.xlk': 'application/x-excel',
  '.xll': 'application/excel',
  '.xll': 'application/vnd.ms-excel',
  '.xll': 'application/x-excel',
  '.xlm': 'application/excel',
  '.xlm': 'application/vnd.ms-excel',
  '.xlm': 'application/x-excel',
  '.xls': 'application/excel',
  '.xls': 'application/vnd.ms-excel',
  '.xls': 'application/x-excel',
  '.xls': 'application/x-msexcel',
  '.xlt': 'application/excel',
  '.xlt': 'application/x-excel',
  '.xlv': 'application/excel',
  '.xlv': 'application/x-excel',
  '.xml': 'text/xml',
  '.xpdl':'text/xml',
  '.xpm': 'image/x-xpixmap',
  '.xsl': 'application/xml',
  '.xul': 'text/xul',
  '.xwd': 'image/x-xwindowdump',
  '.zip': 'application/zip',
};

fallback = "text/plain";

class MimeType:
  def __init__(self, path):
    self.basename = os.path.basename(path);
    self.path = path;
    self.ext = os.path.splitext(self.basename)[-1].lower();

  def mimetype(self):
    global base_lookups
    global fallback

    if base_lookups.has_key(self.ext):
      return base_lookups.get(self.ext);

    return fallback;

if __name__ == "__main__":
  f=MimeType("test.txt");
  f2=MimeType("test.eps");
  print f.mimetype()
  print f2.mimetype()