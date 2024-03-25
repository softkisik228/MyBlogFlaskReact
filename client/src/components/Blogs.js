import React from "react";
import '../css/Blogs.css';
import Blog from "./Blog";

const Blogs = () =>{
    return (
        <div className="Blogs">
            <hr className="hr-line"></hr>
            <div id="main-colnum"><Blog/></div>
        </div>  
    );
}

export default Blogs;