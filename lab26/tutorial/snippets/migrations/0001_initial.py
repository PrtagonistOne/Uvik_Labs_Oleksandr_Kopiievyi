# Generated by Django 4.1.5 on 2023-01-30 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('lineos', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('abap', 'ABAP'), ('abnf', 'ABNF'), ('actionscript', 'ActionScript'), ('actionscript3', 'ActionScript 3'), ('ada', 'Ada'), ('adl', 'ADL'), ('agda', 'Agda'), ('aheui', 'Aheui'), ('alloy', 'Alloy'), ('ambienttalk', 'AmbientTalk'), ('amdgpu', 'AMDGPU'), ('ampl', 'Ampl'), ('ansys', 'ANSYS parametric design language'), ('antlr', 'ANTLR'), ('antlr-actionscript', 'ANTLR With ActionScript Target'), ('antlr-cpp', 'ANTLR With CPP Target'), ('antlr-csharp', 'ANTLR With C# Target'), ('antlr-java', 'ANTLR With Java Target'), ('antlr-objc', 'ANTLR With ObjectiveC Target'), ('antlr-perl', 'ANTLR With Perl Target'), ('antlr-python', 'ANTLR With Python Target'), ('antlr-ruby', 'ANTLR With Ruby Target'), ('apacheconf', 'ApacheConf'), ('apl', 'APL'), ('applescript', 'AppleScript'), ('arduino', 'Arduino'), ('arrow', 'Arrow'), ('arturo', 'Arturo'), ('asc', 'ASCII armored'), ('aspectj', 'AspectJ'), ('aspx-cs', 'aspx-cs'), ('aspx-vb', 'aspx-vb'), ('asymptote', 'Asymptote'), ('augeas', 'Augeas'), ('autohotkey', 'autohotkey'), ('autoit', 'AutoIt'), ('awk', 'Awk'), ('bare', 'BARE'), ('basemake', 'Base Makefile'), ('bash', 'Bash'), ('batch', 'Batchfile'), ('bbcbasic', 'BBC Basic'), ('bbcode', 'BBCode'), ('bc', 'BC'), ('bdd', 'Bdd'), ('befunge', 'Befunge'), ('berry', 'Berry'), ('bibtex', 'BibTeX'), ('blitzbasic', 'BlitzBasic'), ('blitzmax', 'BlitzMax'), ('bnf', 'BNF'), ('boa', 'Boa'), ('boo', 'Boo'), ('boogie', 'Boogie'), ('brainfuck', 'Brainfuck'), ('bst', 'BST'), ('bugs', 'BUGS'), ('c', 'C'), ('c-objdump', 'c-objdump'), ('ca65', 'ca65 assembler'), ('cadl', 'cADL'), ('camkes', 'CAmkES'), ('capdl', 'CapDL'), ('capnp', "Cap'n Proto"), ('cbmbas', 'CBM BASIC V2'), ('cddl', 'CDDL'), ('ceylon', 'Ceylon'), ('cfc', 'Coldfusion CFC'), ('cfengine3', 'CFEngine3'), ('cfm', 'Coldfusion HTML'), ('cfs', 'cfstatement'), ('chaiscript', 'ChaiScript'), ('chapel', 'Chapel'), ('charmci', 'Charmci'), ('cheetah', 'Cheetah'), ('cirru', 'Cirru'), ('clay', 'Clay'), ('clean', 'Clean'), ('clojure', 'Clojure'), ('clojurescript', 'ClojureScript'), ('cmake', 'CMake'), ('cobol', 'COBOL'), ('cobolfree', 'COBOLFree'), ('coffeescript', 'CoffeeScript'), ('comal', 'COMAL-80'), ('common-lisp', 'Common Lisp'), ('componentpascal', 'Component Pascal'), ('console', 'Bash Session'), ('coq', 'Coq'), ('cplint', 'cplint'), ('cpp', 'C++'), ('cpp-objdump', 'cpp-objdump'), ('cpsa', 'CPSA'), ('cr', 'Crystal'), ('crmsh', 'Crmsh'), ('croc', 'Croc'), ('cryptol', 'Cryptol'), ('csharp', 'C#'), ('csound', 'Csound Orchestra'), ('csound-document', 'Csound Document'), ('csound-score', 'Csound Score'), ('css', 'CSS'), ('css+django', 'CSS+Django/Jinja'), ('css+genshitext', 'CSS+Genshi Text'), ('css+lasso', 'CSS+Lasso'), ('css+mako', 'CSS+Mako'), ('css+mozpreproc', 'CSS+mozpreproc'), ('css+myghty', 'CSS+Myghty'), ('css+php', 'CSS+PHP'), ('css+ruby', 'CSS+Ruby'), ('css+smarty', 'CSS+Smarty'), ('css+ul4', 'CSS+UL4'), ('cuda', 'CUDA'), ('cypher', 'Cypher'), ('cython', 'Cython'), ('d', 'D'), ('d-objdump', 'd-objdump'), ('dart', 'Dart'), ('dasm16', 'DASM16'), ('debcontrol', 'Debian Control file'), ('debsources', 'Debian Sourcelist'), ('delphi', 'Delphi'), ('devicetree', 'Devicetree'), ('dg', 'dg'), ('diff', 'Diff'), ('django', 'Django/Jinja'), ('docker', 'Docker'), ('doscon', 'MSDOS Session'), ('dpatch', 'Darcs Patch'), ('dtd', 'DTD'), ('duel', 'Duel'), ('dylan', 'Dylan'), ('dylan-console', 'Dylan session'), ('dylan-lid', 'DylanLID'), ('earl-grey', 'Earl Grey'), ('easytrieve', 'Easytrieve'), ('ebnf', 'EBNF'), ('ec', 'eC'), ('ecl', 'ECL'), ('eiffel', 'Eiffel'), ('elixir', 'Elixir'), ('elm', 'Elm'), ('elpi', 'Elpi'), ('emacs-lisp', 'EmacsLisp'), ('email', 'E-mail'), ('erb', 'ERB'), ('erl', 'Erlang erl session'), ('erlang', 'Erlang'), ('evoque', 'Evoque'), ('execline', 'execline'), ('extempore', 'xtlang'), ('ezhil', 'Ezhil'), ('factor', 'Factor'), ('fan', 'Fantom'), ('fancy', 'Fancy'), ('felix', 'Felix'), ('fennel', 'Fennel'), ('fift', 'Fift'), ('fish', 'Fish'), ('flatline', 'Flatline'), ('floscript', 'FloScript'), ('forth', 'Forth'), ('fortran', 'Fortran'), ('fortranfixed', 'FortranFixed'), ('foxpro', 'FoxPro'), ('freefem', 'Freefem'), ('fsharp', 'F#'), ('fstar', 'FStar'), ('func', 'FunC'), ('futhark', 'Futhark'), ('gap', 'GAP'), ('gap-console', 'GAP session'), ('gas', 'GAS'), ('gcode', 'g-code'), ('gdscript', 'GDScript'), ('genshi', 'Genshi'), ('genshitext', 'Genshi Text'), ('gherkin', 'Gherkin'), ('glsl', 'GLSL'), ('gnuplot', 'Gnuplot'), ('go', 'Go'), ('golo', 'Golo'), ('gooddata-cl', 'GoodData-CL'), ('gosu', 'Gosu'), ('graphviz', 'Graphviz'), ('groff', 'Groff'), ('groovy', 'Groovy'), ('gsql', 'GSQL'), ('gst', 'Gosu Template'), ('haml', 'Haml'), ('handlebars', 'Handlebars'), ('haskell', 'Haskell'), ('haxe', 'Haxe'), ('haxeml', 'Hxml'), ('hexdump', 'Hexdump'), ('hlsl', 'HLSL'), ('hsail', 'HSAIL'), ('hspec', 'Hspec'), ('html', 'HTML'), ('html+cheetah', 'HTML+Cheetah'), ('html+django', 'HTML+Django/Jinja'), ('html+evoque', 'HTML+Evoque'), ('html+genshi', 'HTML+Genshi'), ('html+handlebars', 'HTML+Handlebars'), ('html+lasso', 'HTML+Lasso'), ('html+mako', 'HTML+Mako'), ('html+myghty', 'HTML+Myghty'), ('html+ng2', 'HTML + Angular2'), ('html+php', 'HTML+PHP'), ('html+smarty', 'HTML+Smarty'), ('html+twig', 'HTML+Twig'), ('html+ul4', 'HTML+UL4'), ('html+velocity', 'HTML+Velocity'), ('http', 'HTTP'), ('hybris', 'Hybris'), ('hylang', 'Hy'), ('i6t', 'Inform 6 template'), ('icon', 'Icon'), ('idl', 'IDL'), ('idris', 'Idris'), ('iex', 'Elixir iex session'), ('igor', 'Igor'), ('inform6', 'Inform 6'), ('inform7', 'Inform 7'), ('ini', 'INI'), ('io', 'Io'), ('ioke', 'Ioke'), ('irc', 'IRC logs'), ('isabelle', 'Isabelle'), ('j', 'J'), ('jags', 'JAGS'), ('jasmin', 'Jasmin'), ('java', 'Java'), ('javascript', 'JavaScript'), ('javascript+cheetah', 'JavaScript+Cheetah'), ('javascript+django', 'JavaScript+Django/Jinja'), ('javascript+lasso', 'JavaScript+Lasso'), ('javascript+mako', 'JavaScript+Mako'), ('javascript+mozpreproc', 'Javascript+mozpreproc'), ('javascript+myghty', 'JavaScript+Myghty'), ('javascript+php', 'JavaScript+PHP'), ('javascript+ruby', 'JavaScript+Ruby'), ('javascript+smarty', 'JavaScript+Smarty'), ('jcl', 'JCL'), ('jlcon', 'Julia console'), ('jmespath', 'JMESPath'), ('js+genshitext', 'JavaScript+Genshi Text'), ('js+ul4', 'Javascript+UL4'), ('jsgf', 'JSGF'), ('jslt', 'JSLT'), ('json', 'JSON'), ('jsonld', 'JSON-LD'), ('jsonnet', 'Jsonnet'), ('jsp', 'Java Server Page'), ('julia', 'Julia'), ('juttle', 'Juttle'), ('k', 'K'), ('kal', 'Kal'), ('kconfig', 'Kconfig'), ('kmsg', 'Kernel log'), ('koka', 'Koka'), ('kotlin', 'Kotlin'), ('kuin', 'Kuin'), ('lasso', 'Lasso'), ('lean', 'Lean'), ('less', 'LessCss'), ('lighttpd', 'Lighttpd configuration file'), ('lilypond', 'LilyPond'), ('limbo', 'Limbo'), ('liquid', 'liquid'), ('literate-agda', 'Literate Agda'), ('literate-cryptol', 'Literate Cryptol'), ('literate-haskell', 'Literate Haskell'), ('literate-idris', 'Literate Idris'), ('livescript', 'LiveScript'), ('llvm', 'LLVM'), ('llvm-mir', 'LLVM-MIR'), ('llvm-mir-body', 'LLVM-MIR Body'), ('logos', 'Logos'), ('logtalk', 'Logtalk'), ('lsl', 'LSL'), ('lua', 'Lua'), ('macaulay2', 'Macaulay2'), ('make', 'Makefile'), ('mako', 'Mako'), ('maql', 'MAQL'), ('markdown', 'Markdown'), ('mask', 'Mask'), ('mason', 'Mason'), ('mathematica', 'Mathematica'), ('matlab', 'Matlab'), ('matlabsession', 'Matlab session'), ('maxima', 'Maxima'), ('mcfunction', 'MCFunction'), ('mcschema', 'MCSchema'), ('meson', 'Meson'), ('mime', 'MIME'), ('minid', 'MiniD'), ('miniscript', 'MiniScript'), ('mips', 'MIPS'), ('modelica', 'Modelica'), ('modula2', 'Modula-2'), ('monkey', 'Monkey'), ('monte', 'Monte'), ('moocode', 'MOOCode'), ('moonscript', 'MoonScript'), ('mosel', 'Mosel'), ('mozhashpreproc', 'mozhashpreproc'), ('mozpercentpreproc', 'mozpercentpreproc'), ('mql', 'MQL'), ('mscgen', 'Mscgen'), ('mupad', 'MuPAD'), ('mxml', 'MXML'), ('myghty', 'Myghty'), ('mysql', 'MySQL'), ('nasm', 'NASM'), ('ncl', 'NCL'), ('nemerle', 'Nemerle'), ('nesc', 'nesC'), ('nestedtext', 'NestedText'), ('newlisp', 'NewLisp'), ('newspeak', 'Newspeak'), ('ng2', 'Angular2'), ('nginx', 'Nginx configuration file'), ('nimrod', 'Nimrod'), ('nit', 'Nit'), ('nixos', 'Nix'), ('nodejsrepl', 'Node.js REPL console session'), ('notmuch', 'Notmuch'), ('nsis', 'NSIS'), ('numpy', 'NumPy'), ('nusmv', 'NuSMV'), ('objdump', 'objdump'), ('objdump-nasm', 'objdump-nasm'), ('objective-c', 'Objective-C'), ('objective-c++', 'Objective-C++'), ('objective-j', 'Objective-J'), ('ocaml', 'OCaml'), ('octave', 'Octave'), ('odin', 'ODIN'), ('omg-idl', 'OMG Interface Definition Language'), ('ooc', 'Ooc'), ('opa', 'Opa'), ('openedge', 'OpenEdge ABL'), ('output', 'Text output'), ('pacmanconf', 'PacmanConf'), ('pan', 'Pan'), ('parasail', 'ParaSail'), ('pawn', 'Pawn'), ('peg', 'PEG'), ('perl', 'Perl'), ('perl6', 'Perl6'), ('phix', 'Phix'), ('php', 'PHP'), ('pig', 'Pig'), ('pike', 'Pike'), ('pkgconfig', 'PkgConfig'), ('plpgsql', 'PL/pgSQL'), ('pointless', 'Pointless'), ('pony', 'Pony'), ('portugol', 'Portugol'), ('postgresql', 'PostgreSQL SQL dialect'), ('postscript', 'PostScript'), ('pot', 'Gettext Catalog'), ('pov', 'POVRay'), ('powershell', 'PowerShell'), ('praat', 'Praat'), ('procfile', 'Procfile'), ('prolog', 'Prolog'), ('promql', 'PromQL'), ('properties', 'Properties'), ('protobuf', 'Protocol Buffer'), ('psql', 'PostgreSQL console (psql)'), ('psysh', 'PsySH console session for PHP'), ('pug', 'Pug'), ('puppet', 'Puppet'), ('pwsh-session', 'PowerShell Session'), ('py+ul4', 'Python+UL4'), ('py2tb', 'Python 2.x Traceback'), ('pycon', 'Python console session'), ('pypylog', 'PyPy Log'), ('pytb', 'Python Traceback'), ('python', 'Python'), ('python2', 'Python 2.x'), ('q', 'Q'), ('qbasic', 'QBasic'), ('qlik', 'Qlik'), ('qml', 'QML'), ('qvto', 'QVTO'), ('racket', 'Racket'), ('ragel', 'Ragel'), ('ragel-c', 'Ragel in C Host'), ('ragel-cpp', 'Ragel in CPP Host'), ('ragel-d', 'Ragel in D Host'), ('ragel-em', 'Embedded Ragel'), ('ragel-java', 'Ragel in Java Host'), ('ragel-objc', 'Ragel in Objective C Host'), ('ragel-ruby', 'Ragel in Ruby Host'), ('rbcon', 'Ruby irb session'), ('rconsole', 'RConsole'), ('rd', 'Rd'), ('reasonml', 'ReasonML'), ('rebol', 'REBOL'), ('red', 'Red'), ('redcode', 'Redcode'), ('registry', 'reg'), ('resourcebundle', 'ResourceBundle'), ('restructuredtext', 'reStructuredText'), ('rexx', 'Rexx'), ('rhtml', 'RHTML'), ('ride', 'Ride'), ('rita', 'Rita'), ('rng-compact', 'Relax-NG Compact'), ('roboconf-graph', 'Roboconf Graph'), ('roboconf-instances', 'Roboconf Instances'), ('robotframework', 'RobotFramework'), ('rql', 'RQL'), ('rsl', 'RSL'), ('ruby', 'Ruby'), ('rust', 'Rust'), ('sarl', 'SARL'), ('sas', 'SAS'), ('sass', 'Sass'), ('savi', 'Savi'), ('scala', 'Scala'), ('scaml', 'Scaml'), ('scdoc', 'scdoc'), ('scheme', 'Scheme'), ('scilab', 'Scilab'), ('scss', 'SCSS'), ('sed', 'Sed'), ('sgf', 'SmartGameFormat'), ('shen', 'Shen'), ('shexc', 'ShExC'), ('sieve', 'Sieve'), ('silver', 'Silver'), ('singularity', 'Singularity'), ('slash', 'Slash'), ('slim', 'Slim'), ('slurm', 'Slurm'), ('smali', 'Smali'), ('smalltalk', 'Smalltalk'), ('smarty', 'Smarty'), ('smithy', 'Smithy'), ('sml', 'Standard ML'), ('snbt', 'SNBT'), ('snobol', 'Snobol'), ('snowball', 'Snowball'), ('solidity', 'Solidity'), ('sophia', 'Sophia'), ('sp', 'SourcePawn'), ('sparql', 'SPARQL'), ('spec', 'RPMSpec'), ('spice', 'Spice'), ('splus', 'S'), ('sql', 'SQL'), ('sql+jinja', 'SQL+Jinja'), ('sqlite3', 'sqlite3con'), ('squidconf', 'SquidConf'), ('srcinfo', 'Srcinfo'), ('ssp', 'Scalate Server Page'), ('stan', 'Stan'), ('stata', 'Stata'), ('supercollider', 'SuperCollider'), ('swift', 'Swift'), ('swig', 'SWIG'), ('systemverilog', 'systemverilog'), ('tads3', 'TADS 3'), ('tal', 'Tal'), ('tap', 'TAP'), ('tasm', 'TASM'), ('tcl', 'Tcl'), ('tcsh', 'Tcsh'), ('tcshcon', 'Tcsh Session'), ('tea', 'Tea'), ('teal', 'teal'), ('teratermmacro', 'Tera Term macro'), ('termcap', 'Termcap'), ('terminfo', 'Terminfo'), ('terraform', 'Terraform'), ('tex', 'TeX'), ('text', 'Text only'), ('thrift', 'Thrift'), ('ti', 'ThingsDB'), ('tid', 'tiddler'), ('tlb', 'Tl-b'), ('tnt', 'Typographic Number Theory'), ('todotxt', 'Todotxt'), ('toml', 'TOML'), ('trac-wiki', 'MoinMoin/Trac Wiki markup'), ('trafficscript', 'TrafficScript'), ('treetop', 'Treetop'), ('tsql', 'Transact-SQL'), ('turtle', 'Turtle'), ('twig', 'Twig'), ('typescript', 'TypeScript'), ('typoscript', 'TypoScript'), ('typoscriptcssdata', 'TypoScriptCssData'), ('typoscripthtmldata', 'TypoScriptHtmlData'), ('ucode', 'ucode'), ('ul4', 'UL4'), ('unicon', 'Unicon'), ('unixconfig', 'Unix/Linux config files'), ('urbiscript', 'UrbiScript'), ('usd', 'USD'), ('vala', 'Vala'), ('vb.net', 'VB.net'), ('vbscript', 'VBScript'), ('vcl', 'VCL'), ('vclsnippets', 'VCLSnippets'), ('vctreestatus', 'VCTreeStatus'), ('velocity', 'Velocity'), ('verilog', 'verilog'), ('vgl', 'VGL'), ('vhdl', 'vhdl'), ('vim', 'VimL'), ('wast', 'WebAssembly'), ('wdiff', 'WDiff'), ('webidl', 'Web IDL'), ('whiley', 'Whiley'), ('wowtoc', 'World of Warcraft TOC'), ('wren', 'Wren'), ('x10', 'X10'), ('xml', 'XML'), ('xml+cheetah', 'XML+Cheetah'), ('xml+django', 'XML+Django/Jinja'), ('xml+evoque', 'XML+Evoque'), ('xml+lasso', 'XML+Lasso'), ('xml+mako', 'XML+Mako'), ('xml+myghty', 'XML+Myghty'), ('xml+php', 'XML+PHP'), ('xml+ruby', 'XML+Ruby'), ('xml+smarty', 'XML+Smarty'), ('xml+ul4', 'XML+UL4'), ('xml+velocity', 'XML+Velocity'), ('xorg.conf', 'Xorg'), ('xquery', 'XQuery'), ('xslt', 'XSLT'), ('xtend', 'Xtend'), ('xul+mozpreproc', 'XUL+mozpreproc'), ('yaml', 'YAML'), ('yaml+jinja', 'YAML+Jinja'), ('yang', 'YANG'), ('zeek', 'Zeek'), ('zephir', 'Zephir'), ('zig', 'Zig')], default='python', max_length=100)),
                ('style', models.CharField(choices=[('abap', 'abap'), ('algol', 'algol'), ('algol_nu', 'algol_nu'), ('arduino', 'arduino'), ('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful'), ('default', 'default'), ('dracula', 'dracula'), ('emacs', 'emacs'), ('friendly', 'friendly'), ('friendly_grayscale', 'friendly_grayscale'), ('fruity', 'fruity'), ('github-dark', 'github-dark'), ('gruvbox-dark', 'gruvbox-dark'), ('gruvbox-light', 'gruvbox-light'), ('igor', 'igor'), ('inkpot', 'inkpot'), ('lilypond', 'lilypond'), ('lovelace', 'lovelace'), ('manni', 'manni'), ('material', 'material'), ('monokai', 'monokai'), ('murphy', 'murphy'), ('native', 'native'), ('nord', 'nord'), ('nord-darker', 'nord-darker'), ('one-dark', 'one-dark'), ('paraiso-dark', 'paraiso-dark'), ('paraiso-light', 'paraiso-light'), ('pastie', 'pastie'), ('perldoc', 'perldoc'), ('rainbow_dash', 'rainbow_dash'), ('rrt', 'rrt'), ('sas', 'sas'), ('solarized-dark', 'solarized-dark'), ('solarized-light', 'solarized-light'), ('staroffice', 'staroffice'), ('stata', 'stata'), ('stata-dark', 'stata-dark'), ('stata-light', 'stata-light'), ('tango', 'tango'), ('trac', 'trac'), ('vim', 'vim'), ('vs', 'vs'), ('xcode', 'xcode'), ('zenburn', 'zenburn')], default='friendly', max_length=100)),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
