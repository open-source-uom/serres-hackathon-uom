import React from 'react';

const ColorizedCanvas = ({ shapes, canvasWidth, canvasHeight }) => {
    const getColor = (shapeIndex) => {
        const hue = shapeIndex * 30 % 360;
        return `hsl(${hue}, 70%, 50%)`;
    };
    console.log(shapes,"HELLOOOO")
    return (
        <div style={{ position: 'relative', width: canvasWidth, height: canvasHeight }}>
            {shapes.map((shape,i) => {
                return shape.map(the_shape=>
                    
                    
                    (<div
                    key={i}
                    style={{
                        position: 'absolute',
                        left: the_shape.position.x + 300,
                        top: the_shape.position.y,
                        width: the_shape.size.width,
                        height: the_shape.size.height,
                        background: getColor(i),
                    }}
                />)
                    
                    )
            }
            )}
                
            
           
        </div>
    );
};

export default ColorizedCanvas;
