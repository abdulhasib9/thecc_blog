import { useEffect, useState } from 'react';
import axios from 'axios';
import log from "eslint-plugin-react/lib/util/log.js";

const ArticleList = () => {
    const [articles, setArticles] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Fetch data from the API
        axios.get('http://127.0.0.1:8000/api/articles/')
            .then((response) => {
                console.log('API Response:', response.data); // Log the response
                if (Array.isArray(response.data)) {
                    setArticles(response.data);
                } else {
                    setError('Data is not in expected array format');
                }
                setLoading(false);
            })
            .catch((error) => {
                console.error('Error fetching articles:', error);
                setError('An error occurred while fetching articles');
                setLoading(false);
            });

    }, []);

    if (loading) return <p>Loading articles...</p>;

    if (error) return <p>{error}</p>;

    return (
        <div>
            <h1>Articles</h1>
            {articles.length === 0 ? (
                <p>No articles found.</p>
            ) : (
                articles.map(article => (
                    <div key={article.id} style={{ border: '1px solid #ddd', margin: '10px', padding: '10px' }}>
                        <h2>{article.title}</h2>
                        <p>{article.short_description}</p>
                        <p>{article.content}</p>

                        <h3>Images</h3>
                        <div style={{ display: 'flex', gap: '10px' }}>
                            {article.images.map(image => (

                                <div key={image.id} style={{ textAlign: 'center' }}>

                                    <img
                                        src={image.image_url}

                                        alt={image.title || 'Article Image'}
                                        style={{ maxWidth: '150px', maxHeight: '150px' }}
                                    />

                                    <p>{image.title}</p>
                                    <p>{image.category}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                ))
            )}
        </div>
    );
};

export default ArticleList;
