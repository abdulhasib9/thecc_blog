import { useEffect, useState } from 'react';
import axios from 'axios';

const CategoryList = () => {
    const [categories, setCategories] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/blog/api/categories/')
            .then(response => {
                setCategories(response.data);
            })
            .catch(error => {
                setError('There was an error fetching the categories!');
                console.error(error);
            });
    }, []);

    return (
        <div>
            {error && <p>{error}</p>}
            <h1>Categories</h1>
            <ul>
                {categories.map(category => (
                    <li key={category.id}>
                        <h3>{category.name}</h3>
                        <p>{category.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CategoryList;
