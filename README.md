# Effects bibliography

A collection of research papers and other resources related to the theory and practice of
computational effects.

## Instructions

* [Pull requests](https://github.com/yallop/effects-bibliography/pulls) welcome!
* You can [**edit the file directly**](https://github.com/yallop/effects-bibliography/edit/master/README.md) also.
* Keep the formatting consistent with the rest.
* End a line with a double space to force a line break.

## Software

* **Eff**: programming language with algebraic effects and handlers  
  by Andrej Bauer and Matija Pretnar  
  ([www](http://www.eff-lang.org/))

* **Eff in F#**: A library for programming with algebraic effects in F#  
  by Nick Palladinos  
  ([www](https://github.com/palladin/Eff))

* **Extensible effects**: a Haskell library for effects  
  by Oleg Kiselyov  
  ([hackage](https://hackage.haskell.org/package/extensible-effects))
  ([www](http://okmij.org/ftp/Haskell/extensible/))

* **Frank**: programming language with first-class handlers, invisible effect variables, and multihandlers  
  by Sam Lindley, Conor McBride and Craig McLaughlin  
  ([www](https://github.com/frank-lang/frank))
  
* **F\***: an ML-like effectful dependently typed functional programming language aimed at program verification  
  ([www](https://fstar-lang.org))

* **Koka**: a function-oriented language with effect inference  
  by Daan Leijen  
  ([www](https://github.com/koka-lang/koka))
  
* **Links effect handlers**: an effect handlers extension for the Links web programming language  
  by Daniel Hillerström and Sam Lindley  
  ([www](https://github.com/links-lang/links))

* **Multicore OCaml**: a multicore + effect handlers extension for OCaml  
  by Stephen Dolan, Anil Madhavapeddy, KC Sivaramakrishnan, Leo White and Jeremy Yallop  
  ([www](https://github.com/ocamllabs/ocaml-multicore/wiki))

* **Scala Effekt**: extensible algebraic effects with handlers in Scala  
  by Jonathan Brachthäuser  
  ([www](http://b-studios.de/scala-effekt/))

* **shonky**: a dynamically typed variant of Frank with C-like syntax  
  by Conor McBride  
  ([www](https://github.com/pigworker/shonky))

## Papers

### 2018

* **Explicit Effect Subtyping** (ESOP 2018)  
  by Amr Hany Saleh, Georgios Karachalias, Matija Pretnar, and Tom Schrijvers  
  ([technical report/extended version](https://lirias.kuleuven.be/bitstream/123456789/616205/1/CW711.pdf))

* **Handle with Care: Relational Interpretation of Algebraic Effects and Handlers** (POPL 2018)  
  by Dariusz Biernacki, Maciej Piróg, Piotr Polesiuk, and Filip Sieczkowski  
  ([pdf](https://bitbucket.org/pl-uwr/aleff-logrel/downloads/popl18e.pdf))
  ([Coq formalisation](https://bitbucket.org/pl-uwr/aleff-logrel))

* **Handling fibred algebraic effects** (POPL 2018)  
  by Danel Ahman  
  ([pdf](https://danelahman.github.io/papers/popl18.pdf))

### 2017

* **Effekt: Extensible Algebraic Effects in Scala** (Scala 2017)  
  by Jonathan Immanuel Brachthäuser and Philipp Schuster  
  ([pdf](http://files.b-studios.de/effekt.pdf))

* **Efficient Compilation of Algebraic Effects and Handlers**  
  by Matija Pretnar, Amr Hany Saleh, Axel Faes, and Tom Schrijvers  
  ([technical report](http://www.cs.kuleuven.be/publicaties/rapporten/cw/CW708.pdf))

* **Structured asynchrony with algebraic effects** (TyDe 2017)  
  by Daan Leijen  
  ([OpenTOC](http://www.sigplan.org/OpenTOC/tyde17.html))
  ([technical report](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/asynceffects-msr-tr-2017-21.pdf))

* **Implementing Algebraic Effects in C (or "Monads for Free in C")** (APLAS 2017)  
  by Daan Leijen  
  ([technical report](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/algeff-in-c-tr-v2.pdf))
  ([GitHub](https://github.com/koka-lang/libhandler))

* **Continuation Passing Style for Effect Handlers** (FSCD 2017)  
  by Daniel Hillerström, Sam Lindley, Robert Atkey, and KC Sivaramakrishnan  
  ([pdf](http://homepages.inf.ed.ac.uk/slindley/papers/handlers-cps.pdf))

* **On the expressive power of user-defined effects: Effect handlers, monadic reflection, delimited control** (ICFP 2017)  
  by Yannick Forster, Ohad Kammar, Sam Lindley, and Matija Pretnar  
  ([arxiv](https://arxiv.org/pdf/1610.09161))

* **Do be do be do** (POPL 2017)  
  by Sam Lindley, Conor McBride, and Craig McLaughlin  
  ([dblp](http://dblp.uni-trier.de/rec/html/conf/popl/LindleyMM17))
  ([arxiv](https://arxiv.org/pdf/1611.09259))

* **Type directed compilation of row-typed algebraic effects** (POPL 2017)  
  by Daan Leijen  
  ([dblp](http://dblp.uni-trier.de/rec/html/conf/popl/Leijen17))

* **No value restriction is needed for algebraic effects and handlers** (J. Funct. Program. 2017)  
  by Ohad Kammar and Matija Pretnar  
  ([dblp](http://dblp.uni-trier.de/rec/html/journals/jfp/KammarP17))
  ([arxiv](https://arxiv.org/pdf/1605.06938))

### 2016

* **Efficient Algebraic Effect Handlers for Prolog** (TPLP/ICLP 2016)  
  by Amr Hany Saleh and Tom Schrijvers  
  ([pdf](https://people.cs.kuleuven.be/~tom.schrijvers/Research/papers/iclp2016a.pdf))

* **Eff Directly in OCaml** (ML Workshop 2016)  
  by Oleg Kiselyov and KC Sivaramakrishnan  
  ([pdf](http://kcsrk.info/papers/eff_ocaml_ml16.pdf))

* **Compiling Links Effect Handlers to the OCaml Backend** (ML Workshop 2016)  
  by Daniel Hillerström, Sam Lindley, and KC Sivaramakrishnan  
  ([pdf](http://kcsrk.info/papers/links_ocaml_ml16.pdf))

* **Liberating effects with rows and handlers** (TyDe 2016)  
  by Daniel Hillerström and Sam Lindley  
  ([pdf](http://homepages.inf.ed.ac.uk/slindley/papers/links-effect.pdf))
  ([dblp](http://dblp.uni-trier.de/rec/html/conf/icfp/HillerstromL16))
  
* **Dependent Types and Fibred Computational Effects** (FoSSaCS 2016)  
  by Danel Ahman, Neil Ghani, and Gordon Plotkin  
  ([pdf](https://danelahman.github.io/papers/fossacs16.pdf))
  ([dblp](http://dblp.org/rec/conf/fossacs/AhmanGP16))

### 2015

* **Fixing Non-determinism** (IFL 2015)  
  by Alexander Vandenbroucke, Tom Schrijvers, and Frank Piessens  
  ([pdf](https://people.cs.kuleuven.be/~tom.schrijvers/Research/papers/ifl2015_post.pdf))

* **Freer monads, more extensible effects** (Haskell 2015)  
  by Oleg Kiselyov and Hiromi Ishii  
  ([pdf](http://okmij.org/ftp/Haskell/extensible/more.pdf))

* **Programming with Algebraic Effects and Handlers** (JLAMP 2015)  
  by Andrej Bauer and Matija Pretnar  
  ([arxiv](http://math.andrej.com/wp-content/uploads/2012/03/eff.pdf))
  ([dblp](http://dblp.uni-trier.de/rec/html/journals/jlp/BauerP15))
  ([doi](http://dx.doi.org/10.1016/j.jlamp.2014.02.001))


* **An Introduction to Algebraic Effects and Handlers** (MFPS 2015)  
  by Matija Pretnar  
  ([dblp](http://dblp.uni-trier.de/rec/html/journals/entcs/Pretnar15))
  ([doi](http://dx.doi.org/10.1016/j.entcs.2015.12.003))
  ([pdf](http://www.eff-lang.org/handlers-tutorial.pdf))


* **Fusion for Free: Efficient Algebraic Effect Handlers** (MPC 2015)  
  by Nicolas Wu and Tom Schrijvers  
  ([pdf](https://people.cs.kuleuven.be/~tom.schrijvers/Research/papers/mpc2015.pdf))


* **Interleaving data and effects** (JFP 2015)  
  by Robert Atkey and Patricia Johann  
  ([dblp](http://dblp.uni-trier.de/rec/html/journals/jfp/AtkeyJ15))
  ([doi](http://dx.doi.org/10.1017/S0956796815000209))
  ([pdf](http://bentnib.org/interleaving.pdf))

### 2014

* **Algebraic effects and effect handlers for idioms and arrows** (WGP 2014)  
  by Sam Lindley  
  ([dblp](http://dblp.uni-trier.de/rec/html/conf/icfp/Lindley14))
  ([doi](http://dx.doi.org/10.1145/2633628.2633636))
  ([pdf](http://homepages.inf.ed.ac.uk/slindley/papers/aeia.pdf))

* **Effect handlers in scope** (Haskell 2014)  
  by Nicolas Wu, Tom Schrijvers and Ralf Hinze  
  ([pdf](http://www.cs.ox.ac.uk/people/nicolas.wu/papers/Scope.pdf))

* **Embedding effect systems in Haskell** (Haskell 2014)  
  by Dominic Orchard and Tomas Petricek  
  ([pdf](https://www.cl.cam.ac.uk/~dao29/publ/haskell14-effects.pdf))

* **The semantic marriage of monads and effects (extended abstract)** (Unpublished, 2014)  
  by Dominic Orchard, Tomas Petricek and Alan Mycroft  
  ([pdf](https://www.cl.cam.ac.uk/~dao29/drafts/ixmonad-eabstract.pdf))

* **Inferring algebraic effects** (LMCS 2014)  
  by Matija Pretnar  
  ([arxiv](http://arxiv.org/pdf/1312.2334.pdf))
  ([dblp](http://dblp.uni-trier.de/rec/html/journals/corr/Pretnar13))
  ([doi](http://dx.doi.org/10.2168/LMCS-10%283:21%292014))


* **An Effect System for Algebraic Effects and Handlers** (LMCS 2014)  
  by Andrej Bauer and Matija Pretnar  
  ([arxiv](http://arxiv.org/pdf/1306.6316.pdf))
  ([dblp](http://dblp.uni-trier.de/rec/html/journals/corr/BauerP13))
  ([doi](http://dx.doi.org/10.2168/LMCS-10%284:9%292014))



### 2013

* **Programming and reasoning with algebraic effects and dependent types** (ICFP 2013)  
  by Edwin Brady  
  ([pdf](https://eb.host.cs.st-andrews.ac.uk/drafts/effects.pdf))


* **The constrained-monad problem** (ICFP 2013)  
  by Neil Sculthorpe, Jan Bracker, George Giorgidze and Andy Gill  
  ([pdf](http://www.cs.rhul.ac.uk/home/ucac009/publications/constrained-monad-problem.pdf))


* **Handlers in action** (ICFP 2013)  
  by Ohad Kammar, Sam Lindley and Nicolas Oury  
  ([pdf](http://homepages.inf.ed.ac.uk/slindley/papers/handlers.pdf)) ([GitHub](https://github.com/slindley/effect-handlers))


* **Extensible effects: an alternative to monad transformers** (Haskell 2013)  
  by Oleg Kiselyov, Amr Sabry and Cameron Swords  
  ([pdf](https://www.cs.indiana.edu/~sabry/papers/exteff.pdf))


* **Handling algebraic effects** (LMCS 2013)  
  by Gordon Plotkin and Matija Pretnar  
  ([arxiv](http://arxiv.org/abs/1312.1399))
  ([dblp](http://dblp.org/rec/journals/corr/PlotkinP13))
  ([doi](http://dx.doi.org/10.2168/LMCS-9%284:23%292013))

### 2012

* **The Frank Manual** (2012)  
  by Conor McBride  
  ([www](https://personal.cis.strath.ac.uk/conor.mcbride/pub/Frank/))

* **Control.Effects** (2012)  
  by Sjoerd Visscher

* **Koka: A Language with Row-Polymorphic Effect Inference** (HOPE 2012)  
  by Daan Leijen

### 2011

* **Idioms are Oblivious, Arrows are Meticulous, Monads are Promiscuous** (ENTCS 2011)  
  by Sam Lindley, Philip Wadler and Jeremy Yallop

* **Lightweight Monadic Programming in ML** (ICFP 2011)  
  by Nikhil Swamy, Nataliya Guts, Daan Leijen and Michael Hicks  
  ([pdf](http://www.cs.umd.edu/~mwh/papers/monadic.pdf))

* **Monads, zippers and views: virtualizing the monad stack** (ICFP 2011)  
  by Tom Schrijvers and Bruno C.d.S. Oliveira

* **Just Do It: Simple Monadic Equational Reasoning** (ICFP 2011)  
  by Jeremy Gibbons and Ralf Hinze

### 2010

* **Monad transformers as monoid transformers** (Theor. Comp. Science 2010)  
  by Mauro Jaskelioff and Eugenio Moggi

* **The Operational Monad Tutorial** (The Monad Reader, 2010)  
  by Heinrich Apfelmus

### 2009

* **Handlers of Algebraic Effects** (ESOP 2009)  
  by Gordon Plotkin and Matija Pretnar  
  ([pdf](http://homepages.inf.ed.ac.uk/gdp/publications/Effect_Handlers.pdf))


* **Parameterised Notions of Computation** (JFP 2009)  
  by Robert Atkey  
  ([pdf](http://bentnib.org/paramnotions-jfp.pdf))


* **Algebras for Parameterised Monads** (CALCO 2009)  
  by Robert Atkey  
  ([pdf](http://bentnib.org/algebras-param-monads.pdf))


### 2008

* **Lightweight Monadic Regions** (Haskell 2008)  
  by Oleg Kiselyov and Chung-chieh Shan

* **A Logic for Algebraic Effects** (LICS 2008)  
  by Gordon Plotkin and Matija Pretnar  
  ([pdf](http://homepages.inf.ed.ac.uk/gdp/publications/Logic_Algebraic_Effects.pdf))

* **What is a Categorical Model of Arrows?** (MSFP 2008)
  by Robert Atkey  
  ([pdf](http://bentnib.org/arrows.pdf))

* **Data types a la carte** (JFP 2008)  
  by Wouter Swierstra  
  ([pdf](http://www.cs.ru.nl/~W.Swierstra/Publications/DataTypesALaCarte.pdf))

### 2007

* **Combining algebraic effects with continuations** (Theor. Comput. Sci. 2007)  
  by Martin Hyland, Paul Blain Levy, Gordon Plotkin and John Power

### 2006

* **Programming Monads Operationally with Unimo** (ICFP 2006)  
  by Chuan-kai Lin

* **Monadic Regions** (JFP 2006)  
  by Matthew Fluet and J. Gregory Morrisett

### 2003

* **A Monadic Multi-stage Metalanguage** (FOSSACS 2003)  
  by Eugenio Moggi and Sonia Fagorzi  
  ([pdf](http://www.disi.unige.it/person/MoggiE/ftp/fossacs03.pdf))

* **Algebraic Operations and Generic Effects** (Applied categorical structures, 2003)  
  by Gordon D. Plotkin and John Power

* **The Marriage of Effects and Monads** (Trans. Comp. Logic, 2003)  
  by Philip Wadler and Peter Thiemann

### 2002

* **Composing Monads Using Coproducts** (ICFP 2002)  
  by Christoph Lüth and Neil Ghani

* **Notions of computation determine monads** (FoSSaCS 2002)  
  by Gordon D. Plotkin and John Power

### 2001

* **Monadic Encapsulation of Effects: A Revised Approach (Extended Version)** (JFP 2001)  
  by Eugenio Moggi and Amr Sabry

* **Adequacy for algebraic effects** (FoSSaCS 2001)  
  by Gordon D. Plotkin and John Power

### 2000

* **Deriving Backtracking Monad Transformers** (ICFP 2000)  
  by Ralf Hinze

* **Monads and Effects** (APPSEM 2000)  
  by Nick Benton, John Hughes and Eugenio Moggi

### 1999

* **Representing layered monads** (POPL 1999)  
  by Andrzej Filinski

### 1995

* **Monad Transformers and Modular Interpreters** (POPL 1995)  
  by Sheng Liang, Paul Hudak and Mark Jones

* **Semantic Lego** (UMI Order No. GAX95-33546, 1995)  
  by David A. Espinosa

* **Monads for functional programming** (1995)  
  Philip Wadler

### 1994

* **Extensible Denotational Language Specifications** (TACS 1994)  
  by Robert Cartwright and Matthias Felleisen

* **Building interpreters by transforming stratified monads** (Unpublished, 1994)  
  by David Espinosa

* **Representing monads** (POPL 1994)  
  by Andrzej Filinski

* **Building Interpreters by Composing Monads** (POPL 1994)  
  by Guy L. Steele, Jr.

* **Monads and composable continuations** (J. Lisp & Symb. Comp. 1994)  
  by Philip Wadler

### 1993

* **Imperative Functional Programming** (POPL 1993)  
  by Simon Peyton Jones and Philip Wadler

* **Combining Monads** (Functional Programming, 1993)  
  by David J. King and Philip Wadler

* **How to Compose Monads** (Thinking Machines Corporation tech. report, 1993)  
  Guy L. Steele, Jr.

* **Modular denotational semantics** (Unpublished, 1993)  
  by David Espinosa

### 1992

* **The essence of functional programming** (POPL 1992)  
  by Philip Wadler

### 1991

 * **Notions of computation and monads** (Information and Computation, 93(1), 1991)  
   by Eugenio Moggi  
   ([pdf](http://www.disi.unige.it/person/MoggiE/ftp/ic91.pdf))


### 1990

* **Comprehending Monads** (Lisp and Functional Programming, 1990)  
  Philip Wadler

* **Abstracting Control** (LFP 1990)  
  by Olivier Danvy and Andrzej Filinski

### 1989

* **Computational lambda-calculus and monads** (LICS 1989)  
  by Eugenio Moggi  
  ([pdf](http://www.disi.unige.it/person/MoggiE/ftp/lics89.pdf))

* **An abstract view of programming languages** (Ed. Uni. Tech Report, 1989)  
  by Eugenio Moggi

### 1988

* **Polymorphic effect systems** (POPL 1988)  
  by John M. Lucassen and David K. Gifford  
  ([pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.73.4916&rep=rep1&type=pdf))

* **The FX-87 Interpreter** (ICCL 1988)  
  by Pierre Jouvelot and David K. Gifford  
  ([doi](https://doi.org/10.1109%2FICCL.1988.13044))


---

Status of links at last commit: [![Build Status](https://travis-ci.org/yallop/effects-bibliography.svg?branch=master)](https://travis-ci.org/yallop/effects-bibliography)
