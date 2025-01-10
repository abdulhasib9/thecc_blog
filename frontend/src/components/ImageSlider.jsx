// ImageSlider.jsx
import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Pagination, Autoplay } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/autoplay';

const ImageSlider = () => {
    const images = [
        '../../public/vite.svg',
        '../../public/a.png',
        'https://source.unsplash.com/featured/?beach',
        'https://source.unsplash.com/featured/?mountains',
        'https://source.unsplash.com/featured/?forest',
    ];

    return (
        <div style={{ width: '80%', margin: '0 auto' }}>
            <Swiper
                modules={[Navigation, Pagination, Autoplay]}
                navigation
                pagination={{ clickable: true }}
                autoplay={{ delay: 3000 }}
                loop={true}
                spaceBetween={20}
                slidesPerView={1}
            >
                {images.map((image, index) => (
                    <SwiperSlide key={index}>
                        <img
                            src={image}
                            alt={`Slide ${index + 1}`}
                            style={{
                                width: '100%',
                                height: '400px',
                                objectFit: 'cover',
                                borderRadius: '8px',
                            }}
                        />
                    </SwiperSlide>
                ))}
            </Swiper>
        </div>
    );
};

export default ImageSlider;
