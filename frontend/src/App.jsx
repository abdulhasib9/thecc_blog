import Blog from "./pages/Blog.jsx";
import {Router, Routes,Route} from "react-router-dom";
import SingleBlog from "./pages/SingleBlog.jsx";


function App() {


  return (


            <Routes>
                <Route path="/" element={<Blog />} />
                <Route path="/articles/:id" element={<SingleBlog />} />
            </Routes>


  )
}

export default App
