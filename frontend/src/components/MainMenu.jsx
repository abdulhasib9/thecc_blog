import { useEffect, useState } from 'react';
import axios from 'axios';

const MainMenu = () => {
    const [menus, setMenus] = useState([]);
    const [menuItems, setMenuItems] = useState([]);

    useEffect(() => {
        fetchMenus();
        fetchMenuItems();
    }, []);

    const fetchMenus = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/blog/api/menus/');
            setMenus(response.data);
        } catch (error) {
            console.error('Error fetching menus:', error);
        }
    };

    const fetchMenuItems = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/blog/api/menu-items/');
            setMenuItems(response.data);
        } catch (error) {
            console.error('Error fetching menu items:', error);
        }
    };

    const renderMenuItems = (parentId) => {
        return menuItems
            .filter(item => item.parent === parentId)
            .map(item => (
                <li key={item.id}>
                    <a href={item.url}>{item.title}</a>
                    <ul>{renderMenuItems(item.id)}</ul>
                </li>
            ));
    };

    return (
        <div>
            {menus.map(menu => (
                <div key={menu.id}>
                    <h2>{menu.name}</h2>
                    <ul>{renderMenuItems(null)}</ul>
                </div>
            ))}
        </div>
    );
};

export default MainMenu;
