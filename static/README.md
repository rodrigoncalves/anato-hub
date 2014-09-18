#Foundation Compass Template

####Requirements

  * [Ruby 1.9](https://www.ruby-lang.org/en/downloads/)
  * [compass](http://compass-style.org/): `gem install compass`
  * [Node.js](http://nodejs.org)
  * [bower](http://bower.io): `npm install bower -g`

####Installation

Clone this repository in your project directory and install the latest version of Foundation:

```bash
$ git clone https://github.com/msfernandes/foundation-sass.git
$ cd foundation-sass/
$ bower install
```
**OBS:** To update Foundation version, execute `bower update`

####Usage

1. Turn On the compass compiler: `compass watch`
2. You can customize the Foundation updating any SASS file in `assests > sass > components`.
3. Whenever a SASS file is changed, it's compiled and the style.css (in `assets > css`) is updated with changes made.

[Test Foundation Components](http://codepen.io/ZURBFoundation/full/olduj/)