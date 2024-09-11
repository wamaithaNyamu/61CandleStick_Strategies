<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/wamaithanyamu/61CandleStick_Strategies">
    <img src="media/1.jpeg" alt="Logo" width="auto" height="auto">
  </a>

<h3 align="left">Using candlesticks to create trading strategies</h3>

  <p align="left">
    The project explores using the ta-lib library which offere inbuilt candlestick functions and indicators to build out different trading strategies
    <br />
    <br />
    <a href="https://github.com/wamaithanyamu/61CandleStick_Strategies">View Demo</a>
    ·
    <a href="https://github.com/wamaithanyamu/61CandleStick_Strategies/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/wamaithanyamu/61CandleStick_Strategies/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
     <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started
You can refer to the C++ core modules found [here](https://github.com/TA-Lib/ta-lib/tree/main/src/ta_func) so as to understand what the python wrapper is doing behind the scenes. Refer to this [link](https://github.com/TA-Lib/ta-lib/blob/f393d2af97e5526a34b2e3f4bdad25d9e44f83ac/src/ta_common/ta_global.c#L125) to understand how a body is defined by Ta-Lib.

### Prerequisites
- Python 3.12+

### Installation
Head to https://github.com/cgohlke/talib-build/releases/tag/v0.4.32 . Download the talib build  that suits your architecture and save the file on the same directory.

- Install Ta_Lib 
```shell
python -m pip install <the-talib-wheel-file>.whl
```

- Install fast api using 
```shell
pip install "fastapi[standard]"
```

- Install dependencies 
```shell
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

- Run the dev server

```shell
fastapi dev app.py
```
API docs: http://127.0.0.1:8000/docs   

- Run the prod server (recommended)

```shell
fastapi run app.py
```



<!-- ROADMAP -->
## Roadmap

- ✅ Two Crows
- ✅ Three Black Crows
- ✅ Three Inside Up/Down
- ✅ Three-Line Strike
- ✅ Three Outside Up/Down
- ✅ Three Stars In The South
- ✅ Three Advancing White Soldiers
- ✅ Abandoned Baby
- ✅ Advance Block
- ✅ Belt-hold
- ✅ Breakaway
- ✅ Closing Marubozu
- ✅ Concealing Baby Swallow
- ✅ Counterattack
- ✅ Dark Cloud Cover
- ✅ Doji
- ✅ Doji Star
- ✅ Dragonfly Doji
- ✅ Engulfing Pattern
- ✅ Evening Doji Star
- ✅ Evening Star
- ✅ Up/Down-gap side-by-side white lines
- ✅ Gravestone Doji
- ✅ Hammer
- ✅ Hanging Man
- ✅ Harami Pattern
- ✅ Harami Cross Pattern
- ✅ High-Wave Candle
- ✅ Hikkake Pattern
- ✅ Modified Hikkake Pattern
- ✅ Homing Pigeon
- ✅ Identical Three Crows
- ✅ In-Neck Pattern
- ✅ Inverted Hammer
- ✅ Kicking
- ✅ Kicking - bull/bear determined by the longer marubozu
- ✅ Ladder Bottom
- ✅ Long Legged Doji
- ✅ Long Line Candle
- ✅ Marubozu
- ✅ Matching Low
- ✅ Mat Hold
- ✅ Morning Doji Star
- ✅ Morning Star
- ✅ On-Neck Pattern
- ✅ Piercing Pattern
- [ ] Rickshaw Man
- [ ] Rising/Falling Three Methods
- [ ] Separating Lines
- [ ] Shooting Star
- [ ] Short Line Candle
- [ ] Spinning Top
- [ ] Stalled Pattern
- [ ] Stick Sandwich
- [ ] Takuri (Dragonfly Doji with very long lower shadow)
- [ ] Tasuki Gap
- [ ] Thrusting Pattern
- [ ] Tristar Pattern
- [ ] Unique 3 River
- [ ] Upside Gap Two Crows
- [ ] Upside/Downside Gap Three Methods

See the [open issues](https://github.com/wamaithanyamu/61CandleStick_Strategies/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/wamaithanyamu/61CandleStick_Strategies/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wamaithanyamu/61CandleStick_Strategies" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Your Name - [@wamaithanyamu](https://twitter.com/wamaithanyamu) - email@email_client.com

Project Link: [https://github.com/wamaithanyamu/61CandleStick_Strategies](https://github.com/wamaithanyamu/61CandleStick_Strategies)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/wamaithanyamu/61CandleStick_Strategies.svg?style=for-the-badge
[contributors-url]: https://github.com/wamaithanyamu/61CandleStick_Strategies/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/wamaithanyamu/61CandleStick_Strategies.svg?style=for-the-badge
[forks-url]: https://github.com/wamaithanyamu/61CandleStick_Strategies/network/members
[stars-shield]: https://img.shields.io/github/stars/wamaithanyamu/61CandleStick_Strategies.svg?style=for-the-badge
[stars-url]: https://github.com/wamaithanyamu/61CandleStick_Strategies/stargazers
[issues-shield]: https://img.shields.io/github/issues/wamaithanyamu/61CandleStick_Strategies.svg?style=for-the-badge
[issues-url]: https://github.com/wamaithanyamu/61CandleStick_Strategies/issues
[license-shield]: https://img.shields.io/github/license/wamaithanyamu/61CandleStick_Strategies.svg?style=for-the-badge
[license-url]: https://github.com/wamaithanyamu/61CandleStick_Strategies/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/wamaithanyamu
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[YouTube Channel Subscribers]:(https://img.shields.io/youtube/channel/subscribers/:channelId)
