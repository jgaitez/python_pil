import logo from './logo.svg';
import './App.css';
import Welcome from './components/Welcome';
import Header from './components/Heder';

function App(props) {
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <Header title = "Props Header Titulo" />
        </div>
        <img src={logo} className="App-logo" alt="logo" />
      <Welcome />
      </header>
    </div>
  );
}

export default App;
