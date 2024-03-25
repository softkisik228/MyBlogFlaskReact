import React from "react";
import '../css/Main.css';
import AddPostForm from "./AddPostForm";

const Main = () =>{
    return (
        <div className="main">
            <div className="text-blocks">
                <div className="block1">
                    <p className="about-text">This is a beginner programmer's blog. In this blog, I'm going to share my successes, as well as receive feedback from more experienced developers.</p>
                </div>
                <div className="block2">
                    <p className="about-text">Now i would like to became a backend developer.</p>
                </div>
                <div className="block3">
                    <p className="about-text">I love kittens and my girlfriend!</p>
                </div>
            </div>
            <AddPostForm/>
        </div>
    );
}

export default Main;