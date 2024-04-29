import { useState, useEffect } from 'react';
import React from "react";
import '../css/Blogs.css';
import Blog from "./Blog";


const  Blogs = () =>{
    const [posts, setPosts] = useState(false);
    console.log(1234);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/get_posts',{
            method: 'GET',   
        }).then(
            res => res.json()
        ).then(
            posts => {setPosts(posts)
            console.log(posts);
        }
        );
        console.log(posts); 
    }
    
    )
    return (
        <div className="Blogs">
            <hr className="hr-line"></hr>
            <div id="main-colnum">
                {(typeof posts === 'undefined') ? 
                (<Blog post={'Loading...'}></Blog>) : (
                posts.map((member, i) => (
                    <Blog post={member[1]}></Blog>)))
                }
            </div>
        </div>  
    );
}

export default Blogs;