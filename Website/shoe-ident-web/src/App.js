import './App.css';
import logo from './images/logo.png'

function App() {
  return (
    <section className="App">
      <div className="header">
        </div>
        <nav ClassName="navMenu">
					<a href="./index.html">
						<img id="logo" src={logo} />
					</a>
					<ul class="options">
						<li><a href="#" class="options">Home</a></li>
						<li><a href="#" class="options">Information</a></li>
						<li><a href="#" class="options"></a>Contact</li>
					</ul>
          <div ClassName="header">
            <p>Sneaker Identifier</p>
          </div>
        </nav>
    </section>
  );
}

export default App;
