// Based on code by Davide P. Cervone.
// original code: https://github.com/mathjax/MathJax/issues/2313
// ifstar version: https://github.com/mathjax/MathJax/issues/2428
MathJax = {
  startup: {
    ready() {
      //
      //  These would be replaced by import commands if you wanted to make
      //  a proper extension.
      //
      const Configuration = MathJax._.input.tex.Configuration.Configuration;
      const CommandMap = MathJax._.input.tex.SymbolMap.CommandMap;
      const Macro = MathJax._.input.tex.Symbol.Macro;
      const TexError = MathJax._.input.tex.TexError.default;
      const ParseUtil = MathJax._.input.tex.ParseUtil.default;
      const expandable = MathJax._.util.Options.expandable;

      const IFSTARMAP = 'ifstarMap';

      //
      //  This function implements an ifstar macro.
      //
      const IfstarFunction = (parser, name, resultstar, resultnostar) => {
        //
        //  Get the macro parameters
        //
        const star = parser.GetStar();          // true if there is a *
        //
        //  Construct the replacement string for the macro
        //
        const macro = [(star ? resultstar : resultnostar)].join('');
        //
        //  Insert the replacement string into the TeX string, and check
        //  that there haven't been too many maxro substitutions (prevent's
        //  infinite loops).
        //
        parser.string = ParseUtil.addArgs(parser, macro, parser.string.slice(parser.i));
        parser.i = 0;
        if (++parser.macroCount > parser.configuration.options.maxMacros) {
          throw new TexError('MaxMacroSub1',
            'MathJax maximum macro substitution count exceeded; ' +
            'is there a recursive macro call?');
        }
      };

      //
      //  The is the configuration for the IfstarConfiguration TeX extension.
      //
      const IfstarConfiguration = Configuration.create('Ifstar', {
        //
        //  Initialize the extension by creating the command map for the
        //  macros defined by \DeclareIfstar, and add the
        //  \DeclareIfstar macro itself.  Then append the
        //  command map to the given configuration as a macro handler
        //
        init(config) {
          const map = new CommandMap(IFSTARMAP, {
            DeclareIfstar: ['Declare_Ifstar']
          }, {
            //
            //  Implements \DeclareIfstar control sequence.
            //
            Declare_Ifstar(parser, name) {
              //
              //  Get the control sequence to define and the starred and
              //  non-starred macros to use.
              //
              let cs = ParseUtil.trimSpaces(parser.GetArgument(name));
              const resultstar = parser.GetArgument(name);
              const resultnostar = parser.GetArgument(name);
              //
              //  Check that the control sequence name is valid
              //
              if (cs.charAt(0) === '\\') cs = cs.substr(1);
              if (!cs.match(/^(.|[a-z]+)$/i)) {  //$ syntax highlighting
                throw new TexError(
                  'IllegalControlSequenceName',
                  'Illegal control sequence name for %1',
                  name
                );
              }
              //
              //  Look up the command map and add the new macro to it using
              //  IfstarFunction as the function and passing it the
              //  given starred and non-starred macros.
              //
              const map = parser.configuration.handlers.retrieve(IFSTARMAP);
              map.add(cs, new Macro(cs, IfstarFunction, [resultstar, resultnostar]));
            }
          });
          config.append(
            Configuration.create('IfstarDefs', { handler: { macro: [IFSTARMAP] } })
          );
        },

        //
        //  Add any user-defined starred/non-starred macros (from the
        //  Ifstar configuration object in the document's
        //  option list), if any.
        //
        config(config, jax) {
          const map = jax.parseOptions.handlers.retrieve(IFSTARMAP);
          const starmacros = jax.parseOptions.options.Ifstar;
          for (const cs of Object.keys(starmacros)) {
            map.add(cs, new Macro(cs, IfstarFunction, starmacros[cs]));
          }
        },

        //
        //  Indicate that Ifstar is a valid option, and can have
        //  any number of definitions.  The format is
        //
        //      name: [starred, non-starred]
        //
        //  where 'name' is the macro name, and starred and non-starred are the
        //  macros to use for the \name macro.  You can include
        //  pre-defined macros here, which will be available without
        //  further configuration.
        //
        options: {
          Ifstar: expandable({})
        }
      });

      MathJax.startup.defaultReady();
    }   // ready
  },    // startup

  tex: {
    packages: { '[+]': ['Ifstar'] },
  }
}


{/* <script
    id="MathJax-script"
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"
></script> */}
