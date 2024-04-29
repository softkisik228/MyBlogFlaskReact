import React from "react";
import '../css/Blog.css';

const Blog = ({post}) =>{
    return (
        <div className="Blog">
            <div>
                {post}
            </div>
        </div>
    );
}

export default Blog;