function Header(props) {
    return (
        <div>
            <h1> {props.title}</h1>
        </div>
    );
}

Header.defaultProps = {
    title : "Titulo Default"
}
export default Header;
