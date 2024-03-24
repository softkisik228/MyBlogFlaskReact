import React from "react";
import '../css/Header.css';

const Header = () =>{
    return (
        <header>
            <div className="header-box">
                <span className="label">soft_kisik228 </span>
                <btn className='button'>About</btn>
                <a className='button' href="https://github.com/softkisik228">Git</a>
                <btn className='button'>Account</btn>
            </div>
        </header>
    );
}

export default Header;